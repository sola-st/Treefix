# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_infer_dtype.py
dtype, val = infer_dtype_from_scalar(data)
assert dtype == "M8[ns]"
