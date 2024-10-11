# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = ((1, 1), (2, 2), (2, 3))
s = Series(data)
assert tuple(s) == data
