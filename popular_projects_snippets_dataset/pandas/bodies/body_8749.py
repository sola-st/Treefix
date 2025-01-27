# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d

# default asarray gives objects
result = np.asarray(arr)
expected = np.array(list(arr), dtype=object)
tm.assert_numpy_array_equal(result, expected)

# to object dtype (same as default)
result = np.asarray(arr, dtype=object)
tm.assert_numpy_array_equal(result, expected)

result = np.asarray(arr, dtype="int64")
tm.assert_numpy_array_equal(result, arr.asi8)

# to other dtypes
msg = r"float\(\) argument must be a string or a( real)? number, not 'Period'"
with pytest.raises(TypeError, match=msg):
    np.asarray(arr, dtype="float64")

result = np.asarray(arr, dtype="S20")
expected = np.asarray(arr).astype("S20")
tm.assert_numpy_array_equal(result, expected)
