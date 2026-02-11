# Rule-Based Chatbot (Task 1 - CODSOFT)

def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")

        elif "your name" in user_input:
            print("🤖 Chatbot: I am a rule-based chatbot created for Task 1.")

        elif "help" in user_input:
            print("🤖 Chatbot: I can answer simple questions like greetings, name, or exit.")

        elif "bye" in user_input or "exit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a nice day 👋")
            break

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()