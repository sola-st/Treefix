# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert com.pandas_dtype(dtype) == DatetimeTZDtype.construct_from_string(dtype)
assert com.pandas_dtype(dtype) == dtype
