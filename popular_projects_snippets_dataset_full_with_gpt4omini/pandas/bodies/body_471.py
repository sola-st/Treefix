# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = DatetimeTZDtype.construct_from_string("datetime64[ns, US/Eastern]")
assert is_dtype_equal(dtype, result)
