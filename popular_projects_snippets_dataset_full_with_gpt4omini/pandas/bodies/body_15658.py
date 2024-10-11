# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 3, np.nan, np.nan, np.nan, 11])

# Provide 'forward' (the default) explicitly here.
expected = Series([1.0, 3.0, 5.0, 7.0, np.nan, 11.0])

result = s.interpolate(method="linear", limit=2, limit_direction="forward")
tm.assert_series_equal(result, expected)

result = s.interpolate(method="linear", limit=2, limit_direction="FORWARD")
tm.assert_series_equal(result, expected)
