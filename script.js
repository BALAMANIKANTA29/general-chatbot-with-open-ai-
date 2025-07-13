const chatWindow = document.getElementById('chat-window');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const newChatBtn = document.getElementById('new-chat-btn');
const viewHistoryBtn = document.getElementById('view-history-btn');
const deleteHistoryBtn = document.getElementById('delete-history-btn');
const historyWindow = document.getElementById('history-window');

const API_BASE = '/api';

function appendMessage(role, message) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);
    messageDiv.textContent = message;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage(message) {
    appendMessage('user', message);
    userInput.value = '';
    try {
        const response = await fetch(API_BASE + '/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message }),
        });
        const data = await response.json();
        if (response.ok) {
            appendMessage('assistant', data.response);
        } else {
            appendMessage('assistant', 'Error: ' + data.error);
        }
    } catch (error) {
        appendMessage('assistant', 'Error: ' + error.message);
    }
}

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (message) {
        sendMessage(message);
    }
});

newChatBtn.addEventListener('click', async () => {
    const response = await fetch(API_BASE + '/chat/new', { method: 'POST' });
    if (response.ok) {
        chatWindow.innerHTML = '';
        historyWindow.classList.add('hidden');
        alert('New chat session started.');
    } else {
        alert('Failed to start new chat session.');
    }
});

viewHistoryBtn.addEventListener('click', async () => {
    if (historyWindow.classList.contains('hidden')) {
        try {
            const response = await fetch(API_BASE + '/history');
            const data = await response.json();
            if (response.ok) {
                historyWindow.innerHTML = '';
                data.history.forEach(entry => {
                    const div = document.createElement('div');
                    div.textContent = `[${entry.role}] ${entry.message}`;
                    historyWindow.appendChild(div);
                });
                historyWindow.classList.remove('hidden');
            } else {
                alert('Failed to fetch history.');
            }
        } catch (error) {
            alert('Error fetching history: ' + error.message);
        }
    } else {
        historyWindow.classList.add('hidden');
    }
});

deleteHistoryBtn.addEventListener('click', async () => {
    if (confirm('Are you sure you want to delete all chat history?')) {
        const response = await fetch(API_BASE + '/history/delete', { method: 'POST' });
        if (response.ok) {
            historyWindow.innerHTML = '';
            historyWindow.classList.add('hidden');
            alert('Chat history deleted.');
        } else {
            alert('Failed to delete chat history.');
        }
    }
});
