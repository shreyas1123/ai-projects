history = []

while True:
    you = input("You: ")

    if you == "bye":
        print("Goodbye!")
        break
    else:
        history.append({"role": "user", "content": you})
        reply = "You said: " + you
        print("Bot: " + reply)
        history.append({"role": "assistant", "content": reply})

print("Total messages:", len(history))