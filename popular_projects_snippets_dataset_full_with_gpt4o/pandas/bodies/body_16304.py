# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see gh-1572
s = Series([1, 2, 3])
s2 = Series(s, dtype=np.int64)

s2[1] = 5
assert s[1] == 5
