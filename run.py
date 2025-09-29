from chatbot.chatbot import SimpleChatBot

def start_chat():
    bot = SimpleChatBot()
    
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            response = bot.get_response(user_input)
            print(f"Chatbot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    start_chat()
