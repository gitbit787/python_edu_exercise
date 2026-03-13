"""
Reference implementation of the number guessing game.
"""

import random


def play_game() -> None:
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        raw = input("Enter your guess: ")
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_game()

