"""
Starter version of a number guessing game.

Fill in the TODOs to complete the project.
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

        # TODO: compare guess to secret and give feedback
        # - If too low, print a message.
        # - If too high, print a message.
        # - If correct, congratulate the user and break out of the loop.
        raise NotImplementedError("Compare guess to secret and give feedback.")


if __name__ == "__main__":
    play_game()

