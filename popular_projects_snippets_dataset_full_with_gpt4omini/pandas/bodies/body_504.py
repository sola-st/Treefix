# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = IntervalDtype("interval[int64, right]")
assert is_dtype_equal(dtype, result)
result = IntervalDtype.construct_from_string("interval[int64, right]")
assert is_dtype_equal(dtype, result)
