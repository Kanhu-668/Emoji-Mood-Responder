def mood_detector():
    print("Welcome to the Python Mood Detector! 🎭")
    print("Type 'exit' anytime to quit.\n")

    mood_responses = {
        "happy": "That's great to hear! 😊",
        "sad": "Cheer up! Here's a hug 🤗",
        "angry": "Take a deep breath 😤",
        "tired": "Rest well! 😴",
        "excited": "Let's celebrate! 🎉"
    }

    while True:
        mood = input("How are you feeling today? ").strip().lower()

        if mood == "exit":
            print("Goodbye! Take care! 👋")
            break

        found = False
        for keyword, response in mood_responses.items():
            if keyword in mood:
                print(response)
                found = True
                break

        if not found:
            print("Hmm... I’m not sure how to respond to that 🤔")

        print()  # Blank line for readability


# Run the program
if __name__ == "__main__":
    mood_detector()
