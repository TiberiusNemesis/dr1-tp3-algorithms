"""Exercise 9: recursive QuickSort."""

# Exercise 9: recursively sort using the last element as pivot.
def quicksort(values: list[int]) -> list[int]:
    result = values.copy()

    def sort(low: int, high: int) -> None:
        if low >= high:
            return
        pivot = result[high]
        pivot_index = low
        for index in range(low, high):
            if result[index] <= pivot:
                result[pivot_index], result[index] = result[index], result[pivot_index]
                pivot_index += 1
        result[pivot_index], result[high] = result[high], result[pivot_index]
        sort(low, pivot_index - 1)
        sort(pivot_index + 1, high)

    sort(0, len(result) - 1)
    return result


if __name__ == "__main__":
    for name, values in (("sorted", [1, 2, 3, 4, 5]),
                         ("reversed", [5, 4, 3, 2, 1]),
                         ("random", [4, 1, 5, 2, 3])):
        print(f"{name}: {values} -> {quicksort(values)}")
