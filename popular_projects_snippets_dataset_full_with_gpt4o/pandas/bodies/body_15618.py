# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_equals.py
s1 = Series(arr, index=idx)
s2 = s1.copy()
assert s1.equals(s2)

s1[1] = 9
assert not s1.equals(s2)
