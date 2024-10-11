# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
# Test that infer_dtype_from_scalar is
# returning correct dtype for int and float.
data = np.dtype(any_int_numpy_dtype).type(12)
dtype, val = infer_dtype_from_scalar(data)
assert dtype == type(data)
