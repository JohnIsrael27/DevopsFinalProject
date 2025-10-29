# Automated Development of Chatbot Application using Jenkins and Docker

## How to run locally (dev)
1. Build + run services:


docker compose up --build

2. Chatbot: http://localhost:5000/chat (POST JSON `{"message":"hello"}`)
3. Jenkins UI: http://localhost:8080

## CI/CD
- Jenkinsfile defines pipeline: tests -> build image -> push to Docker Hub
