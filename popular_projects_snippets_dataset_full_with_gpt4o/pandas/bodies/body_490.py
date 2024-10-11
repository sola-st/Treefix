# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_dtype_equal(dtype, "period[D]")
assert is_dtype_equal(dtype, PeriodDtype("D"))
assert is_dtype_equal(dtype, PeriodDtype("D"))
assert is_dtype_equal(PeriodDtype("D"), PeriodDtype("D"))

assert not is_dtype_equal(dtype, "D")
assert not is_dtype_equal(PeriodDtype("D"), PeriodDtype("2D"))
