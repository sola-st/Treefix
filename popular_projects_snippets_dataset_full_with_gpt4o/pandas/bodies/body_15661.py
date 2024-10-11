# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# These tests are for issue #9218 -- fill NaNs in both directions.
s = Series([np.nan, np.nan, 3, np.nan, np.nan, np.nan, 7, np.nan, np.nan])

expected = Series([np.nan, np.nan, 3.0, 4.0, 5.0, 6.0, 7.0, np.nan, np.nan])
result = s.interpolate(method="linear", limit_area="inside")
tm.assert_series_equal(result, expected)

expected = Series(
    [np.nan, np.nan, 3.0, 4.0, np.nan, np.nan, 7.0, np.nan, np.nan]
)
result = s.interpolate(method="linear", limit_area="inside", limit=1)
tm.assert_series_equal(result, expected)

expected = Series([np.nan, np.nan, 3.0, 4.0, np.nan, 6.0, 7.0, np.nan, np.nan])
result = s.interpolate(
    method="linear", limit_area="inside", limit_direction="both", limit=1
)
tm.assert_series_equal(result, expected)

expected = Series([np.nan, np.nan, 3.0, np.nan, np.nan, np.nan, 7.0, 7.0, 7.0])
result = s.interpolate(method="linear", limit_area="outside")
tm.assert_series_equal(result, expected)

expected = Series(
    [np.nan, np.nan, 3.0, np.nan, np.nan, np.nan, 7.0, 7.0, np.nan]
)
result = s.interpolate(method="linear", limit_area="outside", limit=1)
tm.assert_series_equal(result, expected)

expected = Series([np.nan, 3.0, 3.0, np.nan, np.nan, np.nan, 7.0, 7.0, np.nan])
result = s.interpolate(
    method="linear", limit_area="outside", limit_direction="both", limit=1
)
tm.assert_series_equal(result, expected)

expected = Series([3.0, 3.0, 3.0, np.nan, np.nan, np.nan, 7.0, np.nan, np.nan])
result = s.interpolate(
    method="linear", limit_area="outside", limit_direction="backward"
)
tm.assert_series_equal(result, expected)

# raises an error even if limit type is wrong.
msg = r"Invalid limit_area: expecting one of \['inside', 'outside'\], got abc"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method="linear", limit_area="abc")
