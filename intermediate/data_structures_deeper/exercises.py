"""
Intermediate / data_structures_deeper / exercises.py

Practice using built-in containers and collections with small, realistic tasks.
"""

from collections import Counter
from typing import Iterable, List, Mapping


def most_common_words(words: Iterable[str], n: int) -> List[str]:
    """
    Return a list of the `n` most common words, in descending frequency order.

    If there are fewer than `n` distinct words, return all of them.
    """
    counts = Counter(words)
    return [word for word, _ in counts.most_common(n)]


def invert_mapping(mapping: Mapping[str, str]) -> Mapping[str, List[str]]:
    """
    Invert a mapping of key -> value into value -> list[keys].

    Example:
        {"a": "x", "b": "x", "c": "y"} -> {"x": ["a", "b"], "y": ["c"]}
    """
    inverted: dict[str, List[str]] = {}
    for key, value in mapping.items():
        inverted.setdefault(value, []).append(key)
    return inverted


if __name__ == "__main__":
    print(most_common_words(["a", "b", "a", "c", "b", "a"], 2))
    print(invert_mapping({"a": "x", "b": "x", "c": "y"}))

