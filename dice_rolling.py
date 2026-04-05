import random

count = 0
while count < 6:

    choice = input ("roll the dice ? (y/n): ").lower()

    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        count += 1
    elif choice == "n":
        print("Maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print("Limit is over. Thanks for playing!")