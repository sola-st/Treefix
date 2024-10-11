# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
dtype, _ = infer_dtype_from_array(arr, pandas_dtype=pandas_dtype)
assert is_dtype_equal(dtype, expected)
