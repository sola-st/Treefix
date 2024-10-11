# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_downcast.py
result = maybe_downcast_to_dtype(arr, dtype)
tm.assert_numpy_array_equal(result, expected)
