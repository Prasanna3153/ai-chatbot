print("AI Chatbot")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Bot: Hello Lakshmi!")
    elif "how are you" in user_input:
        print("Bot: I am fine. How can I help you?")
    elif "bye" in user_input:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
