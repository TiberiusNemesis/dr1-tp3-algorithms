"""Exercise 5: recursive team combinations."""

# Exercise 5: generate each team once, preserving candidate order.
def teams(candidates: str, k: int) -> list[str]:
    """Return distinct size-k combinations of candidate characters."""
    if not isinstance(candidates, str):
        raise TypeError("candidates must be a string")

    unique_candidates = list(dict.fromkeys(candidates))
    if k < 0 or k > len(unique_candidates):
        return []

    def choose(start: int, remaining: int, prefix: str) -> list[str]:
        if remaining == 0:
            return [prefix]
        if len(unique_candidates) - start < remaining:
            return []

        combinations = []
        for position in range(start, len(unique_candidates)):
            combinations.extend(
                choose(position + 1, remaining - 1, prefix + unique_candidates[position])
            )
        return combinations

    return choose(0, k, "")


if __name__ == "__main__":
    for candidates, size in (("ABCD", 2), ("ABCD", 3), ("AABC", 2)):
        print(f"teams({candidates!r}, {size}) = {teams(candidates, size)}")
