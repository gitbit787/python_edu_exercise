"""
01_basics / solutions.py

Reference solutions for the basics exercises.
"""


def add_two_numbers(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def repeat_text(text: str, times: int) -> str:
    """Return text repeated `times` times, concatenated together."""
    return text * times


def is_even(number: int) -> bool:
    """Return True if number is even, otherwise False."""
    return number % 2 == 0


if __name__ == "__main__":
    print(add_two_numbers(2, 3))
    print(repeat_text("hi", 3))
    print(is_even(4), is_even(5))

