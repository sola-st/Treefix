# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
dtype = any_real_numpy_dtype
expected = np.array([1, 2])
arr = np.array([1.0, 2.0], dtype=dtype)

result = maybe_downcast_to_dtype(arr, "infer")
tm.assert_almost_equal(result, expected, check_dtype=False)
