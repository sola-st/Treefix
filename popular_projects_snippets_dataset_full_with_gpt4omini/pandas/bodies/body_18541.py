# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
# GH#46460
arr = np.arange(5, dtype="i8")
result = tz_convert_from_utc(arr, tz=UTC)
tm.assert_numpy_array_equal(result, arr)
assert not np.shares_memory(arr, result)

result = tz_convert_from_utc(arr, tz=None)
tm.assert_numpy_array_equal(result, arr)
assert not np.shares_memory(arr, result)
