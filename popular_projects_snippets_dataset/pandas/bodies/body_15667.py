# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# These test are for issue #11115 -- limit ends properly.
s = Series([np.nan, np.nan, 5, 7, np.nan, np.nan])

expected = Series([np.nan, np.nan, 5.0, 7.0, 7.0, np.nan])
result = s.interpolate(method="linear", limit=1, limit_direction="forward")
tm.assert_series_equal(result, expected)

expected = Series([np.nan, 5.0, 5.0, 7.0, np.nan, np.nan])
result = s.interpolate(method="linear", limit=1, limit_direction="backward")
tm.assert_series_equal(result, expected)

expected = Series([np.nan, 5.0, 5.0, 7.0, 7.0, np.nan])
result = s.interpolate(method="linear", limit=1, limit_direction="both")
tm.assert_series_equal(result, expected)
