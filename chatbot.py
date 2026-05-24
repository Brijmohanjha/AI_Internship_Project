from datetime import datetime

print("="*50)
print("      STUDENT ASSISTANT CHATBOT")
print("="*50)
print("Type 'bye' to exit")
print()

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Welcome to Student Assistant ChatBot")

    elif "name" in user:
        print("Bot: My name is Student Assistant Bot")

    elif "course" in user or "aiml" in user:
        print("Bot: AIML stands for Artificial Intelligence and Machine Learning")

    elif "subject" in user:
        print("Bot: Your subjects are ML, COA, ADA and Discrete Mathematics")

    elif "college" in user:
        print("Bot: Study regularly and maintain attendance")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time =", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date =", current_date)

    elif "help" in user:
        print("Bot: I can help with basic student queries")

    elif "thank" in user:
        print("Bot: You are welcome!")

    elif user == "bye":
        print("Bot: Thank you! Goodbye")
        break

    else:
        print("Bot: Sorry, I don't understand your question")