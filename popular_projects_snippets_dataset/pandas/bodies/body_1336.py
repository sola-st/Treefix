# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 17193
s_orig = Series([0, 1, 2, 3])
expected = Series([0, -1, -2, 3])

s = s_orig.copy()
s.iloc[Series([1, 2])] = [-1, -2]
tm.assert_series_equal(s, expected)

s = s_orig.copy()
s.iloc[Index([1, 2])] = [-1, -2]
tm.assert_series_equal(s, expected)
