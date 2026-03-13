"""
02_variables_and_types / lesson.py

Examples showing how variables and basic types work in Python.
"""


def run_examples() -> None:
    # Variable assignment
    age = 30
    print("Age:", age)

    # Reassignment
    age = age + 1
    print("Age after a birthday:", age)

    # Different types
    name = "Alice"
    height_meters = 1.7
    is_student = False

    print("Name:", name)
    print("Height (m):", height_meters)
    print("Is student:", is_student)

    # Type conversion
    year_str = "2026"
    year_int = int(year_str)
    print("Year as string:", year_str, "-> as int:", year_int)

    # Building a message with f-strings
    message = f"{name} is {age} years old and {height_meters} meters tall."
    print(message)


if __name__ == "__main__":
    run_examples()

