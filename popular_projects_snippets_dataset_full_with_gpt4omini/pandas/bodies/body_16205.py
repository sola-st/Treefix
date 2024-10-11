# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
ts = Series([3, 4, 5, 6, 7], [3, 4, 5, 6, 7], dtype=float)
expected = [True, True, False, True, True]
assert tm.equalContents(ts.index != 5, expected)
assert tm.equalContents(~(ts.index == 5), expected)
