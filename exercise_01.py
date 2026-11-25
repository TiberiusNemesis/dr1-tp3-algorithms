"""Exercise 1: recursive multiplication by addition."""

# Exercise 1: multiply integers using recursive addition.
def mult(x: int, y: int) -> int:
    """Multiply two integers, showing calls, additions, and returns."""
    print(f"call mult({x}, {y})")

    if y == 0:
        result = 0
    elif y < 0:
        result = -mult(x, -y)
    elif x < 0:
        result = -mult(-x, y)
    else:
        partial = mult(x, y - 1)
        # Exercise 1: addition happens here as the recursive call returns.
        result = x + partial
        print(f"add {x} + {partial} = {result}")

    print(f"return mult({x}, {y}) -> {result}")
    return result


if __name__ == "__main__":
    result = mult(3, 4)
    print(f"mult(3, 4) = {result}")
    print("Addition occurs as recursive calls return.")
