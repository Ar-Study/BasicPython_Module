import random

def guess_number():
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")

guess_number()

# Yang dipelajari dari project ini:
# 1. Library
# 2. Function
# 3. Perulangan
# 4. If Else
