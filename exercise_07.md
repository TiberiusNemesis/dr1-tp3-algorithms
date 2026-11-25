# Exercise 7: Recursive Knapsack Complexity

The selected algorithm is the recursive knapsack function in `exercise_07.py`.
For each weight, it explores two choices: include the weight or skip it. A
branch stops when its remaining target becomes negative or there are no more
weights to consider.

## Redundant calls

Different choices can reach the same remaining target and position. For
example, with a target of 13 and weights `[2, 2, ...]`, including the first
weight and skipping the second reaches the same state `(11, 2)` as skipping
the first and including the second. The function recalculates that state and
its descendants on both paths.

## Number of calls

Running `python3 exercise_07.py` produces these results for a target of 13 and
weights equal to 2:

| Number of weights | Recursive calls |
| ---: | ---: |
| 6 | 127 |
| 9 | 1,003 |
| 12 | 6,603 |

The number of calls grows as more weights are considered. Some branches stop
early when the remaining target becomes negative, so the actual count depends
on the target and weights.

## Big O

In the worst case, each item generates two recursive branches. The decision
tree therefore has O(2^n) calls for n weights. The recursion stack uses O(n)
space, excluding the returned combinations. Listing and storing combinations
can require additional exponential time and space because there can be
exponentially many valid results.
