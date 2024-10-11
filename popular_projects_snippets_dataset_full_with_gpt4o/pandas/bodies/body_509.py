# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_dtype_equal(dtype, "interval[int64, right]")
assert is_dtype_equal(dtype, IntervalDtype("int64", "right"))
assert is_dtype_equal(
    IntervalDtype("int64", "right"), IntervalDtype("int64", "right")
)

assert not is_dtype_equal(dtype, "interval[int64]")
assert not is_dtype_equal(dtype, IntervalDtype("int64"))
assert not is_dtype_equal(
    IntervalDtype("int64", "right"), IntervalDtype("int64")
)

assert not is_dtype_equal(dtype, "int64")
assert not is_dtype_equal(
    IntervalDtype("int64", "neither"), IntervalDtype("float64", "right")
)
assert not is_dtype_equal(
    IntervalDtype("int64", "both"), IntervalDtype("int64", "left")
)

# invalid subtype comparisons do not raise when directly compared
dtype1 = IntervalDtype("float64", "left")
dtype2 = IntervalDtype("datetime64[ns, US/Eastern]", "left")
assert dtype1 != dtype2
assert dtype2 != dtype1
