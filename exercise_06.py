"""Exercise 6: recursive exact-sum knapsack."""

# Exercise 6: recursively include or exclude each weight once.
def knapsack(target: int, weights: list[int], index: int = 0) -> list[list[int]]:
    """Return exact-sum combinations in include-first order."""
    if index < 0 or index > len(weights):
        raise IndexError("index must identify a position in weights or its end")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be nonnegative")

    def search(remaining: int, position: int) -> list[list[int]]:
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
    for target, weights in ((5, [1, 2, 3, 4]), (6, [2, 3, 4, 5])):
        print(f"target={target}, weights={weights}: {knapsack(target, weights)}")
