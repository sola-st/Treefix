# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# These test are for issue #10420 -- flow back to beginning.
s = Series([np.nan, np.nan, 5, 7, 9, np.nan])

expected = Series([5.0, 5.0, 5.0, 7.0, 9.0, np.nan])
result = s.interpolate(method="linear", limit=2, limit_direction="backward")
tm.assert_series_equal(result, expected)

expected = Series([5.0, 5.0, 5.0, 7.0, 9.0, 9.0])
result = s.interpolate(method="linear", limit=2, limit_direction="both")
tm.assert_series_equal(result, expected)
