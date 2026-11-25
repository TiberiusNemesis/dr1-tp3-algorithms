"""Exercise 12: compare QuickSort and QuickSelect."""

from dataclasses import dataclass


@dataclass
class QuickMetrics:
    comparisons: int = 0
    copies: int = 0


# Exercise 12: partition shared by QuickSort and QuickSelect.
def partition(values: list[int], low: int, high: int, metrics: QuickMetrics) -> int:
    pivot = values[high]
    pivot_index = low

    def swap(first: int, second: int) -> None:
        if first != second:
            values[first], values[second] = values[second], values[first]
            metrics.copies += 3

    for index in range(low, high):
        metrics.comparisons += 1
        if values[index] <= pivot:
            swap(pivot_index, index)
            pivot_index += 1
    swap(pivot_index, high)
    return pivot_index


# Exercise 12: sort the entire list for comparison.
def quicksort(values: list[int], *, metrics: QuickMetrics | None = None) -> list[int]:
    result = values.copy()
    if metrics is None:
        metrics = QuickMetrics()

    def sort(low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(result, low, high, metrics)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(result) - 1)
    return result


# Exercise 12: select one rank for comparison.
def quickselect(values: list[int], k: int, *, metrics: QuickMetrics | None = None) -> int:
    if not 0 <= k < len(values):
        raise IndexError("QuickSelect index out of range")
    result = values.copy()
    if metrics is None:
        metrics = QuickMetrics()

    def select(low: int, high: int) -> int:
        if low == high:
            return result[low]
        pivot_index = partition(result, low, high, metrics)
        if k == pivot_index:
            return result[k]
        if k < pivot_index:
            return select(low, pivot_index - 1)
        return select(pivot_index + 1, high)

    return select(0, len(result) - 1)


if __name__ == "__main__":
    for name, values in (("sorted", [1, 2, 3, 4, 5]),
                         ("reversed", [5, 4, 3, 2, 1]),
                         ("random", [4, 1, 5, 2, 3])):
        sort_metrics = QuickMetrics()
        select_metrics = QuickMetrics()
        quicksort(values, metrics=sort_metrics)
        quickselect(values, len(values) // 2, metrics=select_metrics)
        print(f"{name}: QuickSort={sort_metrics.comparisons}/{sort_metrics.copies}, "
              f"QuickSelect={select_metrics.comparisons}/{select_metrics.copies} "
              "comparisons/copies")
    print("QuickSelect finds one rank; QuickSort orders the entire list.")
