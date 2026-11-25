"""Exercise 10: QuickSort comparisons and copies."""

from dataclasses import dataclass


@dataclass
class QuickMetrics:
    comparisons: int = 0
    copies: int = 0


# Exercise 10: count comparisons and three copies for each swap.
def quicksort(values: list[int], *, metrics: QuickMetrics | None = None) -> list[int]:
    result = values.copy()
    if metrics is None:
        metrics = QuickMetrics()

    def swap(first: int, second: int) -> None:
        if first != second:
            result[first], result[second] = result[second], result[first]
            metrics.copies += 3

    def sort(low: int, high: int) -> None:
        if low >= high:
            return
        pivot = result[high]
        pivot_index = low
        for index in range(low, high):
            metrics.comparisons += 1
            if result[index] <= pivot:
                swap(pivot_index, index)
                pivot_index += 1
        swap(pivot_index, high)
        sort(low, pivot_index - 1)
        sort(pivot_index + 1, high)

    sort(0, len(result) - 1)
    return result


if __name__ == "__main__":
    for name, values in (("sorted", [1, 2, 3, 4, 5]),
                         ("reversed", [5, 4, 3, 2, 1]),
                         ("random", [4, 1, 5, 2, 3])):
        metrics = QuickMetrics()
        result = quicksort(values, metrics=metrics)
        print(f"{name}: {result}, comparisons={metrics.comparisons}, copies={metrics.copies}")
    print("A swap between different positions counts as three copies.")
