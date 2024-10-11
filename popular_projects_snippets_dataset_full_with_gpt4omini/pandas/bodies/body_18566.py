# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
# All of these datetime strings with offsets are equivalent
# to the same datetime after the timezone offset is added.
arr = np.array(["01-01-2013 00:00:00"], dtype=object)
expected, _ = tslib.array_to_datetime(arr)

arr = np.array([dt_string], dtype=object)
result, result_tz = tslib.array_to_datetime(arr)

tm.assert_numpy_array_equal(result, expected)
assert result_tz == timezone(timedelta(minutes=expected_tz))
