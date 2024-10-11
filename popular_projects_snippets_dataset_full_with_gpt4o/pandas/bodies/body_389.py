# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert com.pandas_dtype(dtype) is PeriodDtype(dtype)
assert com.pandas_dtype(dtype) == PeriodDtype(dtype)
assert com.pandas_dtype(dtype) == dtype
