# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
dt_string = "01-01-2013T00:00:00.000000000+0000"
arr = np.array([dt_string], dtype=object)

result, result_tz = tslib.array_to_datetime(arr)
expected = np.array([np.datetime64("2013-01-01 00:00:00.000000000")])

tm.assert_numpy_array_equal(result, expected)
assert result_tz is timezone.utc
