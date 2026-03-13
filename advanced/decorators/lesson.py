"""
Advanced / decorators / lesson.py

Examples demonstrating how decorators work.
"""

from functools import wraps
from time import perf_counter


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        duration = perf_counter() - start
        print(f"{func.__name__} took {duration:.6f}s")
        return result

    return wrapper


@timing
def slow_add(a: int, b: int) -> int:
    total = 0
    for _ in range(100000):
        total += a + b
    return total


if __name__ == "__main__":
    print(slow_add(2, 3))

