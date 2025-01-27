# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# boolean series (test for fixing #17294)
ser = Series(input)
result = ser.diff()
expected = Series(output)
tm.assert_series_equal(result, expected)
