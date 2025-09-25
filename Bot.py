while True:
    #user input
    user =  input("you:")
    if user.lower() =="bye":
        print("bot: goodbye! have a nice day.")
        break
    elif "hello" in user.lower():
        print("bot: hi there! how are you?")
    elif"fine" in user.lower() or "good" in user.lower():
        print("bot: Thats's great to hear!")
    elif"name" in user.lower():
        print("bot: i don,t have an age, i live in your computer!")
    else:
        sprint("bot: i don't understand that yet.")            
