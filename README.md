# 🤖 Smart AI CLI Assistant (Ollama Edition)

Smart AI CLI Assistant is a Python-based command-line chatbot that runs locally using a Large Language Model powered by Ollama. It enables users to interact with an AI assistant directly from the terminal without requiring external APIs or cloud services. The project demonstrates how local AI systems can be integrated into lightweight applications using Python and HTTP-based communication.

## Features
- Fully local AI chatbot (no API keys required)
- Conversation memory support
- Interactive CLI interface
- Command system (/help, /history, /clear, /exit)
- Offline AI inference using Ollama
- Error handling for model/server issues

## Technologies Used
Python 3.8+, Ollama (Local LLM runtime), TinyLLaMA model, requests (HTTP communication), colorama (terminal styling)

## Installation

First install Ollama from https://ollama.com/download and pull a model:
ollama run tinyllama

## Clone the repository:
git clone https://github.com/your-username/smart-ai-cli-assistant.git
cd smart-ai-cli-assistant

## Create a virtual environment:
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

## Install dependencies:
pip install -r requirements.txt

## Usage
Run the application:
python3 main.py

Example interaction:
You: What is Python?
AI: Python is a high-level programming language known for simplicity and readability.

You: What is forex trading?
AI: Forex trading is the exchange of currencies in a global financial market.

## Commands
/help → Show available commands
/history → Show conversation history
/clear → Clear memory
/exit → Exit the application

## Configuration
Inside main.py you can change the model:
model: tinyllama

Other options include llama3, mistral, phi3 (depending on system memory).

Ollama API endpoint:
http://localhost:11434/api/chat

## Project Structure
smart-ai-cli-assistant/
├── main.py
├── requirements.txt
├── README.md
├── chat_history.txt (optional)
└── venv/

## Troubleshooting
If model fails (500 error), use tinyllama and ensure enough RAM is available. If Ollama is not found, reinstall from official website. If port 11434 is in use, Ollama is already running.

## Contributing
Fork the repo, create a branch, commit changes, and submit a pull request.

## License
MIT License

## Learning Outcomes
This project demonstrates local AI integration using Ollama, CLI application design in Python, prompt engineering basics, HTTP-based AI communication, debugging system-level AI issues, and working with lightweight LLMs.

This project replaces cloud-based AI APIs with a fully local system powered by Ollama, making it free, offline-capable, and lightweight.
