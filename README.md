# 🛡️ SafeSpace — Women's Safety Chatbot

SafeSpace is an AI-powered chatbot designed to support women and girls facing harassment, abuse, or unsafe situations. It provides a judgment-free space to talk, offers practical safety advice, shares helpline resources, and assesses the severity of the situation in real time.

---

## Features

- **Empathetic Conversations** — The bot listens without judgment and responds with care and understanding
- **Situation Assessment** — Automatically rates the severity of the described situation as LOW, MODERATE, HIGH, or CRITICAL
- **Severity Badge** — Each response includes a color-coded badge so the user immediately understands how serious their situation is
- **Actionable Suggestions** — Provides practical steps the user can take based on what they share
- **Helpline Resources** — Surfaces relevant emergency and support helpline numbers when appropriate
- **Persistent Chat Session** — Maintains conversation context throughout the session for coherent, continuous support
- **Keyboard Friendly** — Press Enter to send, Shift+Enter for a new line

---

## Severity Levels

| Badge | Level | Meaning |
|-------|-------|---------|
| 🟢 | LOW | Uncomfortable situation or mild harassment — awareness needed |
| 🟡 | MODERATE | Repeated harassment or threatening behavior — action recommended |
| 🟠 | HIGH | Stalking, physical threat, or immediate danger possible |
| 🔴 | CRITICAL | Immediate physical danger or assault — emergency services needed |

The CRITICAL badge pulses to draw urgent attention.

---

## Tech Stack

- **Frontend** — HTML, CSS, Vanilla JavaScript
- **Backend** — Python (Flask)
- **AI** — Google Gemini 1.5 Flash via `google-generativeai`
- **Config** — `python-dotenv` for environment variable management

---

## Getting Started

### Prerequisites

- Python 3.8+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone or navigate to the project folder
cd women-safety-chatbot

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Open the `.env` file and replace the placeholder with your actual Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### Running the App

```bash
python app.py
```

Then open your browser and go to `http://localhost:5000`

---

## Project Structure

```
women-safety-chatbot/
├── app.py               # Flask backend, Gemini API integration
├── templates/
│   └── index.html       # Chat UI
├── static/
│   ├── style.css        # Styling and severity badge animations
│   └── script.js        # Chat logic, message rendering
├── .env                 # API key (not committed to version control)
└── requirements.txt     # Python dependencies
```

---

## Important Notes

- This chatbot is a support tool and does not replace professional help or emergency services
- In a life-threatening situation, always call your local emergency number (e.g., 911, 112, 100)
- Global domestic violence helpline: **1-800-799-7233** (US)
- The chatbot does not store or log any conversations

---

## License

This project is built for educational and social good purposes.
