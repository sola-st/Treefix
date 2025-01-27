# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_ndarray.py
arr = np.arange(5, dtype=np.int64).view(dtype)
expected = np.array(list(arr), dtype=object)
assert all(isinstance(x, type(arr[0])) for x in expected)

result = sanitize_array(arr, index=None, dtype=np.dtype(object))
tm.assert_numpy_array_equal(result, expected)
