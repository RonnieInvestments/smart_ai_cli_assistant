import requests
from colorama import Fore, init

init(autoreset=True)

# Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/chat"

# Conversation memory
chat_history = []

def ask_ai(messages):
    try:
        enhanced_messages = [
            {
                "role": "system",
                "content": "You are a precise, helpful AI assistant. Answer clearly and stay on topic."
            }
        ] + messages

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "tinyllama",
                "messages": enhanced_messages,
                "stream": False
            }
        )

        return response.json()["message"]["content"]

    except Exception as e:
        return f"Error: {e}"

def show_help():
    print(Fore.MAGENTA + """
📌 Commands:
/help     Show help
/history  Show conversation
/clear    Clear memory
/exit     Quit
""")

def show_history():
    if not chat_history:
        print(Fore.YELLOW + "No history yet.\n")
        return

    print(Fore.CYAN + "\n📜 Chat History:\n")
    for msg in chat_history:
        role = "You" if msg["role"] == "user" else "AI"
        print(f"{role}: {msg['content']}")
    print()

def main():
    print(Fore.YELLOW + "🤖 Smart AI CLI Assistant (Ollama Edition)")
    print(Fore.YELLOW + "Type /help for commands\n")

    while True:
        user_input = input(Fore.BLUE + "You: ").strip()

        if not user_input:
            print(Fore.RED + "Please enter something.\n")
            continue

        # Commands
        if user_input == "/exit":
            print(Fore.YELLOW + "Goodbye 👋")
            break

        elif user_input == "/help":
            show_help()
            continue

        elif user_input == "/history":
            show_history()
            continue

        elif user_input == "/clear":
            chat_history.clear()
            print(Fore.YELLOW + "Memory cleared!\n")
            continue

        # Add user message
        chat_history.append({"role": "user", "content": user_input})

        print(Fore.MAGENTA + "⏳ Thinking...\n")

        # Get AI response
        response = ask_ai(chat_history)

        # Add AI response
        chat_history.append({"role": "assistant", "content": response})

        print(Fore.GREEN + f"AI: {response}\n")

if __name__ == "__main__":
    main()