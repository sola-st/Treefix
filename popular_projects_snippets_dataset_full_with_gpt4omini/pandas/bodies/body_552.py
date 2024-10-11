# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
dtype = float_numpy_dtype
data = [1.0, 2.0, np.nan]

expected = np.array(data, dtype=dtype)
arr = np.array(data, dtype=dtype)

result = maybe_downcast_to_dtype(arr, "infer")
tm.assert_almost_equal(result, expected)
