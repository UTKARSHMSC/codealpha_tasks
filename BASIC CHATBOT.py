import nltk
from nltk.chat.util import Chat, reflections
import time

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm good, thanks! How about you?", "Doing well, what about you?"]],
    [r"what is your name", ["I'm a chatbot powered by NLTK!", "Call me Jarvis!"]],
    [r"how old are you", ["I am 21 years old!"]],
    [r"connect me to the server", ["Okay sir, connecting to the server now!"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm not sure how to respond to that.", "Can you rephrase that?"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm an NLP-powered chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "time" in user_input:  # Check for time-related queries
            print(f"Chatbot: The current time is {time.ctime()}")
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat()
