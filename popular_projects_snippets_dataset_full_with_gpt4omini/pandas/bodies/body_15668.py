# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 2, 3])
result = s.interpolate(method="polynomial", order=1)
tm.assert_series_equal(result, s)

# non-scipy
result = s.interpolate()
tm.assert_series_equal(result, s)
