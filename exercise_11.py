"""Exercise 11: recursive QuickSelect."""

from dataclasses import dataclass


@dataclass
class QuickMetrics:
    comparisons: int = 0
    copies: int = 0


# Exercise 11: select one zero-based rank using recursive partitioning.
def quickselect(values: list[int], k: int, *, metrics: QuickMetrics | None = None) -> int:
    if not 0 <= k < len(values):
        raise IndexError("QuickSelect index out of range")
    result = values.copy()
    if metrics is None:
        metrics = QuickMetrics()

    def swap(first: int, second: int) -> None:
        if first != second:
            result[first], result[second] = result[second], result[first]
            metrics.copies += 3

    def select(low: int, high: int) -> int:
        if low == high:
            return result[low]
        pivot = result[high]
        pivot_index = low
        for index in range(low, high):
            metrics.comparisons += 1
            if result[index] <= pivot:
                swap(pivot_index, index)
                pivot_index += 1
        swap(pivot_index, high)
        if k == pivot_index:
            return result[k]
        if k < pivot_index:
            return select(low, pivot_index - 1)
        return select(pivot_index + 1, high)

    return select(0, len(result) - 1)


if __name__ == "__main__":
    values = [9, 1, 8, 2, 7, 3, 6]
    index = len(values) // 2
    metrics = QuickMetrics()
    median = quickselect(values, index, metrics=metrics)
    print(f"values={values}, median index={index}, median={median}")
    print(f"comparisons={metrics.comparisons}, copies={metrics.copies}")
