# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# object series
ser = Series([False, True, 5.0, np.nan, True, False])
result = ser.diff()
expected = ser - ser.shift(1)
tm.assert_series_equal(result, expected)
