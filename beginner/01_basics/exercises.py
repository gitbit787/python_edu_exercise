"""
01_basics / exercises.py

Implement the functions below. Run the tests (once added) or write your own
prints to check that your solutions behave as expected.
"""


def add_two_numbers(a: int, b: int) -> int:
    """Return the sum of a and b."""
    # TODO: you can re-implement this yourself
    return a + b


def repeat_text(text: str, times: int) -> str:
    """Return text repeated `times` times, concatenated together."""
    # TODO: you can re-implement this yourself
    return text * times


def is_even(number: int) -> bool:
    """Return True if number is even, otherwise False."""
    # TODO: you can re-implement this yourself
    return number % 2 == 0


if __name__ == "__main__":
    # Quick manual checks (you can modify these)
    print(add_two_numbers(2, 3))       # expected: 5
    print(repeat_text("hi", 3))        # expected: "hihihi"
    print(is_even(4), is_even(5))      # expected: True False

