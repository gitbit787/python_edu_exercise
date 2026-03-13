"""
Intermediate / data_structures_deeper / solutions.py

Reference implementations for the data structures exercises.
"""

from collections import Counter
from typing import Iterable, List, Mapping


def most_common_words(words: Iterable[str], n: int) -> List[str]:
    counts = Counter(words)
    return [word for word, _ in counts.most_common(n)]


def invert_mapping(mapping: Mapping[str, str]) -> Mapping[str, List[str]]:
    inverted: dict[str, List[str]] = {}
    for key, value in mapping.items():
        inverted.setdefault(value, []).append(key)
    return inverted


if __name__ == "__main__":
    print(most_common_words(["a", "b", "a", "c", "b", "a"], 2))
    print(invert_mapping({"a": "x", "b": "x", "c": "y"}))

