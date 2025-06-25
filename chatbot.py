import datetime
import re

# Fun facts list and tracker
fun_facts = [
    "Did you know? Honey never spoils — archaeologists found 3,000-year-old edible honey in Egypt!",
    "Octopuses have three hearts and blue blood!",
    "Bananas are berries, but strawberries aren't!",
    "The Eiffel Tower can grow taller in summer due to heat expansion.",
    "There are more stars in the universe than grains of sand on Earth."
]
fun_fact_index = 0  # Global tracker

# Function to get a response from the bot
def get_bot_response(user_input):
    global fun_fact_index
    user_input = user_input.strip().lower()

    if re.search(r"\b(hi|hey|hello|hola|hlo)\b", user_input):
        return "Hello! How can I help you today?"
    elif re.search(r"\bhow are you\b", user_input):
        return "I'm just a bot, but I'm doing great!"
    elif re.search(r"\bwhat is your name\b", user_input):
        return "I'm a simple rule-based chatbot."
    elif "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {user_name}!"
    elif re.search(r"\btime\b", user_input):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."
    elif re.search(r"\bdate\b", user_input):
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome!"
    elif re.search(r"\b(sad|upset|unhappy)\b", user_input):
        return "I'm sorry to hear that. I'm here if you want to talk!"
    elif re.search(r"\b(happy|excited|joy)\b", user_input):
        return "Yay! I'm glad you're feeling great!"
    elif re.search(r"\b(who am i)\b", user_input):
        return "You're someone amazing!"
    elif re.search(r"\b(motivate me|i feel low|need motivation)\b", user_input):
        return "You're doing great! Every little step forward is a victory. 💪"
    elif "tell me a fun fact" in user_input:
        fun_fact_index = 0
        return fun_facts[fun_fact_index]
    elif "more fun facts" in user_input or "tell me more" in user_input:
        fun_fact_index += 1
        if fun_fact_index < len(fun_facts):
            return fun_facts[fun_fact_index]
        else:
            return "That's all the fun facts I have for now!"
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "Hmm... I didn't get that. Try asking about time, date, or say 'tell me a fun fact'."

# Function to save chat history
def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"You: {user_input}\nBot: {bot_response}\n\n")

# Main function
def main():
    print("🤖 Chatbot: Hi! I'm your assistant bot.")
    print("Ask me anything. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please say something!")
            continue

        response = get_bot_response(user_input)
        print("Bot:", response)
        log_conversation(user_input, response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

# Run the chatbot
if __name__ == "__main__":
    main()
