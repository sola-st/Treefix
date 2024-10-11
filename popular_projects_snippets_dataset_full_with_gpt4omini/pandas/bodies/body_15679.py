# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# Explicit cast to float to avoid implicit cast when setting np.nan
s = Series(np.arange(10) ** 2, dtype="float")
s[np.random.randint(0, 9, 3)] = np.nan
result1 = s.interpolate(method="spline", order=1)
expected1 = s.interpolate(method="spline", order=1)
tm.assert_series_equal(result1, expected1)
