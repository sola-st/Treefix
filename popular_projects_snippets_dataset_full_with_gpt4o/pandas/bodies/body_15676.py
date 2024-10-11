# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 2, np.nan, 4, 5, np.nan, 7])
result = s.interpolate(method="spline", order=1)
expected = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
tm.assert_series_equal(result, expected)
