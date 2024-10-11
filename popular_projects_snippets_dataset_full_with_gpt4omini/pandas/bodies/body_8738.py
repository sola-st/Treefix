# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = TimedeltaArray(timedelta_index)

# default asarray gives the same underlying data
result = np.asarray(arr)
expected = arr._ndarray
assert result is expected
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, copy=False)
assert result is expected
tm.assert_numpy_array_equal(result, expected)

# specifying m8[ns] gives the same result as default
result = np.asarray(arr, dtype="timedelta64[ns]")
expected = arr._ndarray
assert result is expected
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype="timedelta64[ns]", copy=False)
assert result is expected
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype="timedelta64[ns]")
assert result is not expected
tm.assert_numpy_array_equal(result, expected)

# to object dtype
result = np.asarray(arr, dtype=object)
expected = np.array(list(arr), dtype=object)
tm.assert_numpy_array_equal(result, expected)

# to other dtype always copies
result = np.asarray(arr, dtype="int64")
assert result is not arr.asi8
assert not np.may_share_memory(arr, result)
expected = arr.asi8.copy()
tm.assert_numpy_array_equal(result, expected)

# other dtypes handled by numpy
for dtype in ["float64", str]:
    result = np.asarray(arr, dtype=dtype)
    expected = np.asarray(arr).astype(dtype)
    tm.assert_numpy_array_equal(result, expected)
