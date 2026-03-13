"""
01_basics / lesson.py

Runnable examples for the first Python basics lesson.
"""


def run_examples() -> None:
    # Printing text
    print("Hello, Python learner!")

    # Basic types
    an_integer = 10
    a_float = 3.14
    a_string = "Python is fun"
    a_boolean = True

    print("Integer:", an_integer)
    print("Float:", a_float)
    print("String:", a_string)
    print("Boolean:", a_boolean)

    # Simple arithmetic
    print("10 + 5 =", an_integer + 5)
    print("10 * 2 =", an_integer * 2)

    # String operations
    greeting = "Hello, " + "world!"
    print(greeting)
    print("Length of greeting:", len(greeting))


if __name__ == "__main__":
    run_examples()

