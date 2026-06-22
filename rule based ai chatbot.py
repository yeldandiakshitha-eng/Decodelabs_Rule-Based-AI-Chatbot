print("=" * 50)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you. 😊")

    elif user == "how are you":
        print("Bot: I am doing great! Thanks for asking. 😄")

    elif user == "your name":
        print("Bot: My name is RuleBot. 🤖")

    elif user == "course":
        print("Bot: I can provide information about AI, ML, Python, and technology courses.")

    elif user == "python":
        print("Bot: Python is a beginner-friendly programming language widely used in AI and Machine Learning.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It enables machines to mimic human intelligence.")

    elif user == "what is ml":
        print("Bot: ML stands for Machine Learning. It allows computers to learn from data.")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    elif user == "help":
        print("\nAvailable Commands:")
        print("• hello / hi / hey")
        print("• how are you")
        print("• your name")
        print("• course")
        print("• python")
        print("• ai")
        print("• ml")
        print("• thank you")
        print("• help")
        print("• bye")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that command. Type 'help' for available commands.")