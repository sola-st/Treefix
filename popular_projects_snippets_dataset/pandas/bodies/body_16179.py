# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH14227
s1 = Series([1, 2], index=[1, 1])
s2 = Series([10, 10], index=[1, 2])
result = s1 + s2
expected = Series([11, 12, np.nan], index=[1, 1, 2])
tm.assert_series_equal(result, expected)
