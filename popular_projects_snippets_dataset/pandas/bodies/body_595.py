# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_ndarray.py
result = sanitize_array(values, index=None, dtype=dtype)
tm.assert_numpy_array_equal(result, expected)
