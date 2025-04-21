import re

def chat(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b":"Hello welcome to the store"

    }

    for pattern,reponse in responses.items():
        if re.search(pattern,user_input):
            return reponse
    
    return "Sorry"

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Happy shopping! 🛍")
        break
    response = chat(user_message)
    print("Chatbot:", response)

