"""
02_variables_and_types / exercises.py

Implement the functions below, using variables, basic types, and conversions.
"""


def format_greeting(name: str, age: int) -> str:
    """Return a friendly greeting like 'Hello Alice, you are 30 years old.'"""
    # TODO: you can re-implement this yourself
    return f"Hello {name}, you are {age} years old."


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return the Body Mass Index (BMI) given weight and height."""
    # TODO: you can re-implement this yourself
    return weight_kg / (height_m ** 2)


def to_boolean(value: str) -> bool:
    """
    Convert a string to a boolean.

    Treat 'true', 'yes', '1' (any case) as True.
    Treat 'false', 'no', '0' (any case) as False.
    For anything else, default to False.
    """
    # TODO: you can re-implement this yourself
    normalized = value.strip().lower()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    return False


if __name__ == "__main__":
    print(format_greeting("Alice", 30))           # example output
    print(calculate_bmi(70.0, 1.75))             # example BMI
    print(to_boolean("YES"), to_boolean("no"))   # expected: True False

