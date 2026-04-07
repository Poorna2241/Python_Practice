import random

rand = random.randint(1, 100)

count = 0

while count < 10:

    try:
        guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    count += 1

    if guess < 100 and guess > 0:
        if guess < rand:
            print("Too low! Try again.")
        elif guess > rand:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")

else:
    print(f"Sorry, you've used all your attempts. The number was {rand}.")