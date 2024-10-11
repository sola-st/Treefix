# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# these test are for issue #16282 default Limit=None is unlimited
s = Series([np.nan, 1.0, 3.0, np.nan, np.nan, np.nan, 11.0, np.nan])
expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
result = s.interpolate(method="linear", limit_direction="both")
tm.assert_series_equal(result, expected)

expected = Series([np.nan, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
result = s.interpolate(method="linear", limit_direction="forward")
tm.assert_series_equal(result, expected)

expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, np.nan])
result = s.interpolate(method="linear", limit_direction="backward")
tm.assert_series_equal(result, expected)
