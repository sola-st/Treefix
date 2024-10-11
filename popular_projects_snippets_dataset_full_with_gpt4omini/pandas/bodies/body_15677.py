# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 2, 3, 4, np.nan, 6, np.nan])
result3 = s.interpolate(method="spline", order=1, ext=3)
expected3 = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0])
tm.assert_series_equal(result3, expected3)

result1 = s.interpolate(method="spline", order=1, ext=0)
expected1 = Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
tm.assert_series_equal(result1, expected1)
