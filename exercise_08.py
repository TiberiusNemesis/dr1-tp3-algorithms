"""Exercise 8: memoized knapsack."""

from dataclasses import dataclass


@dataclass
class CallStats:
    """Count calls, evaluations, and memoization cache hits."""

    calls: int = 0
    evaluations: int = 0
    cache_hits: int = 0


# Exercise 8: use the same input validation for both versions.
def _validate(weights: list[int], index: int) -> None:
    if index < 0 or index > len(weights):
        raise IndexError("index must identify a position in weights or its end")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be nonnegative")


# Exercise 8: recursively solve knapsack without memoization.
def knapsack(target: int, weights: list[int], index: int = 0, *,
             stats: CallStats | None = None) -> list[list[int]]:
    """Return exact-sum combinations with a plain recursive search."""
    _validate(weights, index)

    def search(remaining: int, position: int) -> list[list[int]]:
        if stats is not None:
            stats.calls += 1
            stats.evaluations += 1
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


# Exercise 8: cache results for each remaining target and index.
def knapsack_memoized(target: int, weights: list[int], index: int = 0, *,
                      stats: CallStats | None = None) -> list[list[int]]:
    """Return exact-sum combinations while reusing cached subproblems."""
    _validate(weights, index)
    cache: dict[tuple[int, int], tuple[tuple[int, ...], ...]] = {}

    def search(remaining: int, position: int) -> tuple[tuple[int, ...], ...]:
        if stats is not None:
            stats.calls += 1
        key = (remaining, position)
        if key in cache:
            if stats is not None:
                stats.cache_hits += 1
            return cache[key]
        if stats is not None:
            stats.evaluations += 1

        if remaining < 0:
            result = ()
        elif position == len(weights):
            result = ((),) if remaining == 0 else ()
        else:
            included = tuple(
                (weights[position], *combination)
                for combination in search(remaining - weights[position], position + 1)
            )
            result = included + search(remaining, position + 1)
        cache[key] = result
        return result

    return [list(combination) for combination in search(target, index)]


if __name__ == "__main__":
    weights = [2] * 12
    plain_stats = CallStats()
    memo_stats = CallStats()
    plain = knapsack(13, weights, stats=plain_stats)
    memo = knapsack_memoized(13, weights, stats=memo_stats)
    print(f"target=13, weights={weights}")
    print(f"plain: result={plain}, calls={plain_stats.calls}")
    print(f"memoized: result={memo}, calls={memo_stats.calls}, "
          f"evaluations={memo_stats.evaluations}, cache hits={memo_stats.cache_hits}")
