import json
from chatbot.app import app

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"

def test_chat_hello():
    client = app.test_client()
    resp = client.post("/chat", json={"message": "hello"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "Hi" in data["reply"] or "demo chatbot" in data["reply"]

def test_chat_echo():
    client = app.test_client()
    msg = "Some random message"
    resp = client.post("/chat", json={"message": msg})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "Echo" in data["reply"]
