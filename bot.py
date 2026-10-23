import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = (os.environ.get("TELEGRAM_TOKEN") or "").strip()
if TOKEN.startswith("bot"):
    TOKEN = TOKEN[3:]
RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL")

@app.route("/")
def home():
    return "Bot Bac Bo está online!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if chat_id and text == "/start" and TOKEN:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "Olá! ❤️ O bot está ligado!"
            },
            timeout=10
        )

    return {"ok": True}

@app.route("/setup", methods=["GET"])
def setup():
    if not TOKEN or not RENDER_URL:
        return "Falta configurar uma variável.", 500

    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/setWebhook",
        json={"url": RENDER_URL.rstrip("/") + "/webhook"},
        timeout=10
    )
    return response.text, response.status_code
@app.route("/teste")
def teste():
    return "TESTE OK"
