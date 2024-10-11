# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
float_numpy_dtype = np.dtype(float_numpy_dtype).type
data = float_numpy_dtype(12)

dtype, val = infer_dtype_from_scalar(data)
assert dtype == float_numpy_dtype
