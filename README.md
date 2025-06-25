# Task 1 - Chatbot 🤖🗨️

This is a simple **rule-based chatbot** created using Python. It responds to basic user queries such as greetings, time/date, emotional states, and even shares fun facts. All conversations are logged into a file for reference.

---

## 💡 Features

- Responds to:
  - Greetings (`hi`, `hello`, etc.)
  - Time and date queries
  - Emotional cues (`happy`, `sad`, etc.)
  - Name introduction (e.g., “my name is Sejal”)
  - Fun facts on request
- Saves chat logs to `chat_log.txt`
- Exits gracefully on commands like `bye`, `exit`, or `quit`
- Lightweight, terminal-based interaction

---

## 📁 Files Included

- `chatbot.py` – Main Python script
- `chat_log.txt` – Automatically created to save chat history
- `README.md` – Project overview and guide

---

## ▶️ How to Run

1. Ensure Python is installed (preferably version 3.6+)
2. Open terminal or command prompt
3. Navigate to the project folder
4. Run the chatbot using:
   ```bash
   python chatbot.py


Example Conversation

You: hi
Bot: Hello! How can I help you today?

You: what is the time now?
Bot: The current time is 03:15 PM.

You: I am sad
Bot: I'm sorry to hear that. I'm here if you want to talk!

You: bye
Bot: Goodbye! Have a great day!
