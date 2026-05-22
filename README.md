# General Chatbot with OpenAI

A full-stack intelligent chatbot application powered by OpenAI's API. This project combines modern web technologies with advanced AI capabilities to create an interactive chat experience.

## 🚀 Features

- **AI-Powered Conversations**: Leverages OpenAI's GPT models for intelligent responses
- **Responsive Web Interface**: Clean, intuitive UI for seamless user interaction
- **Real-time Chat**: Instant message processing and responses
- **User-Friendly Design**: Modern styling with smooth interactions
- **Backend API Integration**: Secure integration with OpenAI services

## 📊 Tech Stack

| Technology | Usage | Percentage |
|-----------|-------|-----------|
| **JavaScript** | Frontend Logic & Interactivity | 37.3% |
| **CSS** | Styling & Layout | 30.3% |
| **Python** | Backend Server & API | 21.2% |
| **HTML** | Page Structure | 11.2% |

### Technologies Used:
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python (Flask/Django or similar framework)
- **API**: OpenAI GPT API
- **Deployment**: Ready for cloud deployment

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - For backend server
- **Node.js** (optional) - For frontend build tools
- **OpenAI API Key** - [Get your API key](https://platform.openai.com/api-keys)
- **Git** - For version control

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BALAMANIKANTA29/general-chatbot-with-open-ai-.git
cd general-chatbot-with-open-ai-
```

### 2. Backend Setup (Python)

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never commit your API key to version control!**

### 4. Frontend Setup

No additional setup needed! Open `index.html` directly in your browser or serve it through a local server.

## 🚀 Usage

### Running the Backend

```bash
python app.py
# or
flask run
```

The backend server will start on `http://localhost:5000` (or your configured port).

### Accessing the Application

1. Open your browser and navigate to `http://localhost:5000`
2. Type your message in the chat input field
3. Press Enter or click Send to interact with the AI
4. View real-time responses from the OpenAI API

## 📁 Project Structure

```
general-chatbot-with-open-ai-/
├── index.html              # Main HTML file
├── style.css               # Styling
├── script.js               # Frontend JavaScript
├── app.py                  # Backend Python server
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🔐 Environment Variables

Create a `.env` file with the following variables:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxx
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

## 📦 Dependencies

### Python Requirements

- flask
- python-dotenv
- openai
- requests
- cors

### JavaScript

No external dependencies required (vanilla JavaScript)

## 🎯 Configuration

Edit the following files to customize:

- **API Model**: Change the GPT model in `app.py` (e.g., `gpt-4`, `gpt-3.5-turbo`)
- **UI Theme**: Modify colors in `style.css`
- **Chat Behavior**: Adjust prompts and parameters in `script.js`

## 🐛 Troubleshooting

### Issue: "Invalid API Key"
- Verify your OpenAI API key in `.env`
- Check that you have active OpenAI credits

### Issue: "Connection Refused"
- Ensure the backend server is running
- Check that the port configuration matches

### Issue: "CORS Error"
- Verify CORS is properly configured in `app.py`
- Check API endpoint URL in `script.js`

## 🚀 Deployment

### Deploy to Heroku

```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Deploy to Vercel (Frontend Only)

```bash
npm install -g vercel
vercel
```

### Deploy to PythonAnywhere (Backend)

1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload files via Web interface
3. Configure your web app settings
4. Set environment variables in the dashboard

## 📝 API Documentation

### Endpoint: `/api/chat`

**Method**: POST

**Request**:
```json
{
  "message": "Your question here"
}
```

**Response**:
```json
{
  "response": "AI-generated response",
  "status": "success"
}
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source. See the LICENSE file for details.

## 💡 Future Enhancements

- [ ] User authentication and chat history
- [ ] Multiple language support
- [ ] Voice input/output capabilities
- [ ] Image generation with DALL-E integration
- [ ] Database integration for persistent storage
- [ ] Advanced conversation context management
- [ ] Rate limiting and usage analytics
- [ ] Mobile app version

## 📞 Support

For issues, questions, or suggestions:

- Open an [Issue](https://github.com/BALAMANIKANTA29/general-chatbot-with-open-ai-/issues)
- Check existing documentation
- Contact the maintainer

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for the GPT API
- [GitHub](https://github.com/) for version control
- All contributors and supporters

---

**Last Updated**: 2025-07-13

Made with ❤️ by [BALAMANIKANTA29](https://github.com/BALAMANIKANTA29)
