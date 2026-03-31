from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are a compassionate and knowledgeable women's safety advisor chatbot.
Your role is to:
1. Listen empathetically to situations involving harassment, abuse, or safety concerns
2. Provide practical, actionable suggestions and safety advice
3. Share relevant helpline numbers when appropriate (e.g. 1-800-799-7233 for domestic violence US, 112 for emergencies)
4. Assess the severity of the situation

At the END of every response, you MUST include a severity block in this exact format (nothing after it):
<severity>{"level": "LOW", "reason": "brief reason"}</severity>

Severity levels:
- LOW: Uncomfortable situation or mild harassment, needs awareness
- MODERATE: Repeated harassment or threatening behavior, action recommended
- HIGH: Stalking, physical threat, immediate danger possible
- CRITICAL: Immediate physical danger or assault, emergency services needed

Always be warm, non-judgmental, and empowering. Never victim-blame."""

chat_histories = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    session_id = data.get("session_id", "default")

    if session_id not in chat_histories:
        chat_histories[session_id] = []

    history = chat_histories[session_id]

    history.append(types.Content(role="user", parts=[types.Part(text=user_message)]))

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=history,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
        )
        full_text = response.text
    except Exception as e:
        err = str(e)
        if "429" in err or "RESOURCE_EXHAUSTED" in err:
            return jsonify({"reply": "I'm a little overwhelmed right now due to high demand. Please wait a moment and try again.", "severity": None})
        return jsonify({"reply": "Something went wrong on my end. Please try again shortly.", "severity": None})

    history.append(types.Content(role="model", parts=[types.Part(text=full_text)]))
    chat_histories[session_id] = history

    severity = None
    display_text = full_text

    if "<severity>" in full_text and "</severity>" in full_text:
        start = full_text.index("<severity>") + len("<severity>")
        end = full_text.index("</severity>")
        severity_json = full_text[start:end].strip()
        display_text = full_text[:full_text.index("<severity>")].strip()
        try:
            severity = json.loads(severity_json)
        except json.JSONDecodeError:
            severity = None

    return jsonify({"reply": display_text, "severity": severity})

if __name__ == "__main__":
    app.run(debug=True)
