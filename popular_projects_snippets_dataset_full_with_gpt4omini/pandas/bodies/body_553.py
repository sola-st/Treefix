# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
dtype = any_real_numpy_dtype
arr = np.array([], dtype=dtype)
result = maybe_downcast_to_dtype(arr, np.dtype("int64"))
tm.assert_numpy_array_equal(result, np.array([], dtype=np.int64))
