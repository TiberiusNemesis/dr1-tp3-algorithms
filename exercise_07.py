"""Exercise 7: recursive knapsack complexity."""

from dataclasses import dataclass


@dataclass
class CallStats:
    """Count recursive calls for complexity analysis."""

    calls: int = 0


# Exercise 7: count calls in the recursive knapsack decision tree.
def knapsack(target: int, weights: list[int], index: int = 0, *,
             stats: CallStats | None = None) -> list[list[int]]:
    """Return exact-sum combinations and count recursive calls."""
    if index < 0 or index > len(weights):
        raise IndexError("index must identify a position in weights or its end")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be nonnegative")

    def search(remaining: int, position: int) -> list[list[int]]:
        if stats is not None:
            stats.calls += 1
        if remaining < 0:
            return []
        if position == len(weights):
            return [[]] if remaining == 0 else []

        included = [
            [weights[position], *combination]
            for combination in search(remaining - weights[position], position + 1)
        ]
        return included + search(remaining, position + 1)

    return search(target, index)


if __name__ == "__main__":
    for size in (6, 9, 12):
        stats = CallStats()
        knapsack(13, [2] * size, stats=stats)
        print(f"weights={size}, calls={stats.calls}")
    print("Repeated states make the decision tree O(2^n) in the worst case.")
