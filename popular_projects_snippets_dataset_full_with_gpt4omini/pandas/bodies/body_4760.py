# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["aafootwo", np.nan, "aabartwo", True, datetime.today(), None, 1, 2.0])
result = ser.str.slice(start, stop, step)
expected = Series(expected)
tm.assert_series_equal(result, expected)
