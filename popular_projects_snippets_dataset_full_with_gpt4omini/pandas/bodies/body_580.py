# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
dtype, val = infer_dtype_from_scalar(bool_val)
assert dtype == np.bool_
