# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
factor = Categorical([0, 1, 2, 0, 1, 2] * 100, ["a", "b", "c"], fastpath=True)
expected = [
    "['a', 'b', 'c', 'a', 'b', ..., 'b', 'c', 'a', 'b', 'c']",
    "Length: 600",
    "Categories (3, object): ['a', 'b', 'c']",
]
expected = "\n".join(expected)

actual = repr(factor)

assert actual == expected
