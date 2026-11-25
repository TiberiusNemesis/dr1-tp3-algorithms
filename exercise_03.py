"""Exercise 3: recursive exponentiation."""

# Exercise 3: raise a number to an integer exponent recursively.
def power(x: float | int, y: int) -> float | int:
    """Use exponentiation by squaring and reciprocals for negative powers."""
    if y == 0:
        return 1
    if y < 0:
        if x == 0:
            raise ZeroDivisionError("zero cannot have a negative exponent")
        return power(1 / x, -y)
    if y == 1:
        return x

    half = power(x, y // 2)
    square = half * half
    return square if y % 2 == 0 else x * square


if __name__ == "__main__":
    for base, exponent in ((2, 10), (-2, 5), (2, -3), (0, 0)):
        print(f"power({base}, {exponent}) = {power(base, exponent)}")
    print("Exponentiation by squaring uses O(log(|y| + 1)) recursive calls.")
