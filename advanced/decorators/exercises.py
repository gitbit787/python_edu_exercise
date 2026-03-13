"""
Advanced / decorators / exercises.py

Implement useful decorators based on the patterns shown in the lesson.
"""

from collections import defaultdict
from functools import wraps
from typing import Any, Callable, Dict, Tuple

Func = Callable[..., Any]


def call_counter(_func: Func | None = None, *, store: Dict[str, int] | None = None):
    """
    Decorator that counts how many times a function is called.

    Usage:
        @call_counter
        def foo(): ...

        @call_counter(store=my_store)
        def bar(): ...
    """

    if store is None:
        store = defaultdict(int)

    def decorator(func: Func) -> Func:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            store[func.__name__] += 1
            return func(*args, **kwargs)

        wrapper.call_counts = store  # type: ignore[attr-defined]
        return wrapper  # type: ignore[return-value]

    if _func is not None:
        return decorator(_func)

    return decorator


if __name__ == "__main__":
    @call_counter
    def greet(name: str) -> str:
        return f"Hello {name}"

    greet("Alice")
    greet("Bob")
    # Access call counts via attribute:
    print(greet.call_counts)  # type: ignore[attr-defined]

