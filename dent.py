import random

num = random.randint(1,100)

print("Hello!, Welcome to the ULTIMATE NUMBER GUESSING GAME.\nYou have 7 attempts.")


for i in range(1,8):
    guess = int(input("Enter your guess: "))
    if num == guess:
        print(f"Congratulation! You got it in {i} attempts")
        break
    elif num > guess:
        print("Try higher")
    elif num < guess:
        print("Try lower.")
    else:
        print("Invalid Input is provided by the user.")
else:
    print("You lost.")






