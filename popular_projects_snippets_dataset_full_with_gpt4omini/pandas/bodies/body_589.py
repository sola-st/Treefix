# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
dtype, _ = infer_dtype_from_scalar(value, pandas_dtype=pandas_dtype)
assert is_dtype_equal(dtype, expected)

with pytest.raises(TypeError, match="must be list-like"):
    infer_dtype_from_array(value, pandas_dtype=pandas_dtype)
