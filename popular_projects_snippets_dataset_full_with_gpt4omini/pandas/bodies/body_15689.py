# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# datetime diff (GH#3100)
ser = Series(date_range("20130102", periods=5))
result = ser.diff()
expected = ser - ser.shift(1)
tm.assert_series_equal(result, expected)

# timedelta diff
result = result - result.shift(1)  # previous result
expected = expected.diff()  # previously expected
tm.assert_series_equal(result, expected)
