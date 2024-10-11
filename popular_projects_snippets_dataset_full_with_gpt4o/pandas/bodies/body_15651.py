# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
sq = Series([1, 4, np.nan, 16], index=[1, 2, 3, 4])
result = sq.interpolate(method="quadratic")
expected = Series([1.0, 4.0, 9.0, 16.0], index=[1, 2, 3, 4])
tm.assert_series_equal(result, expected)
