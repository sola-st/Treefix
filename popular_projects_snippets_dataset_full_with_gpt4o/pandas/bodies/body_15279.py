# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH35747 - Selecting values when a Series has an Index of frozenset
idx0, idx1 = frozenset("a"), frozenset("b")
s = Series([1, 2], index=[idx0, idx1])
assert s[idx0] == 1
assert s[idx1] == 2
s[idx1] = 3
assert s[idx1] == 3
