def main():
    color1 = "gray"
    color2 = "pink"
    print(f"1) Roll a ball using {color1}")
    choice1 = input("long body or round body? ")
    if choice1 == "long body":
        print("2) Roll the ball into an egg shape.")
    else:
        print("2) Keep it as a ball.")
    print(f"3) Roll a smaller ball using {color1} for the head.")
    print("4) Attach the head to one end of the body.")
    choice2 = input("long tail or short tail? ")
    if choice2 == "long tail":
        print(f"5) Roll a thin rope using {color2} and attach to the back.")
    else:
        print(f"5) Add a small bump using {color2} to the back.")
    print(f"6) Add four small legs to the bottom using {color1}.")
    print("7) Add two dots for eyes and a tony nose.")
    print("8) Name this creation 'Mouse'.")


if __name__ == "__main__":
    main()
