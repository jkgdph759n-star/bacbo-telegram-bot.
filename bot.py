
import os
import requests
from flask import Flask

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")

@app.route("/")
def home():
    return "Bot Bac Bo está online!"

@app.route("/webhook", methods=["POST"])
def webhook():
    from flask import request
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat = message.get("chat", {})
    text = message.get("text", "")
    chat_id = chat.get("id")

    if chat_id and text == "/start":
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "Olá! ❤️ O bot está ligado. Ainda estamos a preparar a análise dos resultados do Bac Bo."
            },
            timeout=10
        )

    return {"ok": True}
