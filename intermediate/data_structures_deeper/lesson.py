"""
Intermediate / data_structures_deeper / lesson.py

Examples of using built-in containers and the collections module.
"""

from collections import Counter, defaultdict, deque


def run_examples() -> None:
    numbers = [1, 2, 2, 3, 3, 3]
    counts = Counter(numbers)
    print("Counts:", counts)

    word_lengths = defaultdict(int)
    for word in ["python", "is", "great"]:
        word_lengths[word] = len(word)
    print("Word lengths:", dict(word_lengths))

    queue = deque()
    queue.append("first")
    queue.append("second")
    print("Queue pop left:", queue.popleft())


if __name__ == "__main__":
    run_examples()

