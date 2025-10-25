# 🎭 Python Mood Detector

A fun and interactive Python program that detects your mood based on your input and responds with an appropriate message! 😄  
Perfect for beginners learning about loops, conditionals, and user input in Python.

---

## 🧠 How It Works
The Mood Detector asks the user how they are feeling and responds with a suitable reaction based on predefined moods.  
If it doesn’t recognize the mood, it gives a friendly default response. You can exit anytime by typing `exit`.

---

## 💻 Features
- Detects common moods like **happy**, **sad**, **angry**, **tired**, and **excited**
- Gives an emoji-based response 🎉  
- Keeps chatting until you type `exit`
- Simple, beginner-friendly code

---

## 🧩 Code Example

```python
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
