def unibuddy_chatbot():
    # Gather user information
    name = input("Hi there! What's your name? ")
    favorite_color = input("Nice to meet you, {}! What's your favorite color? ".format(name))
    age = input("Great choice! How old are you? ")

    # Personalized greeting based on favorite color
    if favorite_color.lower() == 'blue':
        print("Blue is a fantastic color, {}! You might enjoy joining the Blue Art Club on campus.".format(name))
    else:
        print("Nice choice, {}! We have a vibrant community here.".format(name))

    # Personalized comment based on age
    age = int(age)
    if age < 18:
        print("Being {} is exciting! There are special freshman events you won't want to miss.".format(age))
    else:
        print("Welcome, {}! You're embarking on an exciting journey at our university.".format(name))

    # Chatbot interaction
    while True:
        query = input("Ask me anything, {}! Type 'exit' to end the conversation: ".format(name))

        if query.lower() == 'exit':
            print("Goodbye, {}! If you have more questions, feel free to ask.".format(name))
            break
        else:
            respond_to_query(query)

def respond_to_query(query):
    # Simple responses for demonstration purposes
    if 'library' in query.lower():
        print("The library is located on the third floor of the main building.")
    elif 'debate club' in query.lower():
        print("To join the debate club, visit the Student Organizations Fair next week.")
    else:
        print("I'm not sure about that, but I'm here to help with anything else!")

# Run the UniBuddy chatbot
unibuddy_chatbot()
