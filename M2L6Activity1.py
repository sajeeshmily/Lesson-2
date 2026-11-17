
import random

print("====================================")
print("       NUMBER GUESSING GAME")
print("====================================")

print("\nI have selected a number between 1 and 50.")
print("You have 5 attempts to guess it!")
print("Let's start the game!\n")

secret_number = random.randint(1, 50)

attempts = 5
won = False

while attempts > 0:

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("\nCongratulations! You guessed correctly!")
        won = True
        break

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Too low! Try a bigger number.")

    attempts = attempts - 1

    print("Lives remaining:", attempts)
    print()

if won:
    print("You won the game!")
else:
    print("Game Over!")
    print("The secret number was:", secret_number)

print("\n====================================")
print("       THANK YOU FOR PLAYING!")
print("====================================")
