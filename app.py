import os
import sqlite3
from flask import Flask, request, jsonify, g
from flask_cors import CORS
from dotenv import load_dotenv
import sys
from google import genai

from flask import render_template

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

DATABASE = 'chat_history.db'

client = genai.Client(api_key=os.getenv("GEMANI_API_KEY"))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def save_message(role, message):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO chats (role, message) VALUES (?, ?)', (role, message))
    db.commit()

def get_chat_history():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT role, message, timestamp FROM chats ORDER BY id ASC')
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

def clear_chat_history():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM chats')
    db.commit()

def call_gemani_ai(messages):
    """
    Use Google GenAI client to generate content with Gemini model.
    """
    # Combine messages into a single string for the 'contents' parameter
    # Here we concatenate user messages for simplicity
    contents = "\n".join([msg['content'] for msg in messages if msg['role'] == 'user'])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
    )
    return response.text

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    # Save user message
    save_message('user', user_message)

    # Prepare messages for Gemani AI
    history = get_chat_history()
    messages = []
    for entry in history:
        messages.append({"role": entry['role'], "content": entry['message']})

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    try:
        bot_message = call_gemani_ai(messages)
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500

    # Save bot response
    save_message('assistant', bot_message)

    return jsonify({'response': bot_message})

@app.route('/api/chat/new', methods=['POST'])
def new_chat():
    clear_chat_history()
    return jsonify({'message': 'Chat history cleared, new session started.'})

@app.route('/api/history', methods=['GET'])
def history():
    history = get_chat_history()
    return jsonify({'history': history})

@app.route('/api/history/delete', methods=['POST'])
def delete_history():
    clear_chat_history()
    return jsonify({'message': 'Chat history deleted.'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
