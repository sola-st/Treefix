# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
expected = [
    "['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c']",
    "Categories (3, object): ['a' < 'b' < 'c']",
]
expected = "\n".join(expected)
actual = repr(factor)
assert actual == expected
