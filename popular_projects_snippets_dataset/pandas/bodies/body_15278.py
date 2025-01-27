# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH 35534 - Selecting values when a Series has an Index of tuples
s = Series([1, 2], index=[("a",), ("b",)])
assert s[("a",)] == 1
assert s[("b",)] == 2
s[("b",)] = 3
assert s[("b",)] == 3
