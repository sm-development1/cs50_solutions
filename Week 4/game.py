# Simple guessing game: computer picks a number 1-100, user guesses until correct.

import random

def main():
    secret = random.randint(1, 100)
    while True:
        try:
            guess = int(input())
        except ValueError:
            # ignore non-integer input and keep asking
            continue
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You got it!")
            break

if __name__ == "__main__":
    main()
