import random


choices = ("r", "p", "s")  # tapples read only
choice_imogies = {"r": "👊", "p": "✋", "s": "✌️"}

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")

def display_choices(user_choice, computer_choice):
    print(f"You chose: {choice_imogies[user_choice]} ({user_choice})")
    print(f"Computer chose: {choice_imogies[computer_choice]} ({computer_choice})")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:

    user_choice = get_user_choice()

    if user_choice not in choices:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)



    result = determine_winner(user_choice, computer_choice)
    print(result)

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == "n":
        print("Thanks for playing! Goodbye!")
        break
