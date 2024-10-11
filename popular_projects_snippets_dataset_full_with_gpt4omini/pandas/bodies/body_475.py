# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_dtype_equal(dtype, "datetime64[ns, US/Eastern]")
assert is_dtype_equal(dtype, "M8[ns, US/Eastern]")
assert is_dtype_equal(dtype, DatetimeTZDtype("ns", "US/Eastern"))
assert not is_dtype_equal(dtype, "foo")
assert not is_dtype_equal(dtype, DatetimeTZDtype("ns", "CET"))
assert not is_dtype_equal(
    DatetimeTZDtype("ns", "US/Eastern"), DatetimeTZDtype("ns", "US/Pacific")
)

# numpy compat
assert is_dtype_equal(np.dtype("M8[ns]"), "datetime64[ns]")

assert dtype == "M8[ns, US/Eastern]"
