"""Exercise 2: recursive integer factorization."""

from math import isqrt


# Exercise 2: recursively factor an integer into prime factors.
def factor(x: int, lowest: int = 2) -> list[int]:
    """Return factors in nondecreasing order, using -1 for a negative input.

    When ``lowest`` is greater than 2, smaller factors must already be removed.
    Zero has no finite prime factorization.
    """
    if lowest < 2:
        raise ValueError("lowest must be at least 2")
    if x == 0:
        raise ValueError("zero has no finite prime factorization")
    if x < 0:
        return [-1, *factor(-x, lowest)]
    if x == 1:
        return []

    for divisor in range(lowest, isqrt(x) + 1):
        if x % divisor == 0:
            return [divisor, *factor(x // divisor, divisor)]
    return [x]


if __name__ == "__main__":
    for value in (84, 13, -84, 1):
        print(f"factor({value}) = {factor(value)}")
    try:
        factor(0)
    except ValueError as error:
        print(f"factor(0) raises ValueError: {error}")
