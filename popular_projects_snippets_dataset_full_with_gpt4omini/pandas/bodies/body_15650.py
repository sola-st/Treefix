# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([0, 1, 2, np.nan], index=list("abcd"))
result = s.interpolate()
expected = Series([0.0, 1.0, 2.0, 2.0], index=list("abcd"))
tm.assert_series_equal(result, expected)
