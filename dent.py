import random

number = random.randint(1, 100)
max_attempts = 7
attempts_used = 0

print("Hello! Welcome to the number guessing game.")
print(f"You have {max_attempts} attempts to guess a number from 1 to 100.")

while attempts_used < max_attempts:
    raw_guess = input("Enter your guess: ").strip()

    try:
        guess = int(raw_guess)
    except ValueError:
        print("Please enter a whole number from 1 to 100.")
        continue

    if not 1 <= guess <= 100:
        print("Please enter a number from 1 to 100.")
        continue

    attempts_used += 1

    if guess == number:
        print(f"Congratulations! You guessed it in {attempts_used} attempts.")
        break
    elif guess < number:
        print("Try higher.")
    else:
        print("Try lower.")
else:
    print(f"You lost. The number was {number}.")
