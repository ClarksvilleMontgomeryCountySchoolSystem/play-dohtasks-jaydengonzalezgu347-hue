def main():
    color1 = "red"
    color2 = "blue"
    print(f"1) Use {color2} to roll a ball.")
    # Collect input. Use choice1 Prompt: "1, 2, or 3? "
    choice1 = input("1, 2, or 3? ")
    if choice1 == "1":
        print("2) Make the ball flat.\n")
    elif choice1 == "2": 
        print("2) Form the ball into an egg shape.\n")
    else: 
        print("2) Keep it round.")
    print(f"3) Use {color2} to roll two thin ropes.")
    # Collect input. Use choice2 Prompt:"A or B? "
    choice2 = input("A or B? ")
    # Use == to check the User's choice.
    # Use the correct string.
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "A":
        print("4) Pinch off pieces of the thin ropes to make and attach spots.\n")
    else:
        print("4) Use the ropes to make stripes.\n")
    print("5) Add two tiny dots for eyes on the front.")
    choice3 = input()
    print(f"6) Write {choice3} on the name card.")

if __name__ == "__main__":
    main()
