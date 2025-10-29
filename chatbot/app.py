from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple rule-based responses
RESPONSES = {
    "hello": "Hi! I'm your demo chatbot. How can I help?",
    "hi": "Hello! Ask me something.",
    "help": "I can echo messages or answer 'hello'. Try sending {\"message\": \"hello\"} as JSON.",
}

def get_response(message: str) -> str:
    msg = message.strip().lower()
    return RESPONSES.get(msg, f"Echo: {message}")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "send JSON with 'message'"}), 400
    return jsonify({"reply": get_response(message)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
