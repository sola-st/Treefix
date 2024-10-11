# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
data = np.dtype(complex_dtype).type(1)
dtype, val = infer_dtype_from_scalar(data)
assert dtype == np.complex_
