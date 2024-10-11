# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 18980
closed = "right" if subtype is not None else None
dtype = IntervalDtype(subtype, closed=closed)
assert is_dtype_equal(dtype, "interval")
assert is_dtype_equal(dtype, IntervalDtype())
