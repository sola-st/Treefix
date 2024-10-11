# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_datetime64tz_dtype(dtype)
assert is_datetime64tz_dtype("datetime64[ns, US/Eastern]")
assert is_datetime64_any_dtype(dtype)
assert is_datetime64_any_dtype("datetime64[ns, US/Eastern]")
assert is_datetime64_ns_dtype(dtype)
assert is_datetime64_ns_dtype("datetime64[ns, US/Eastern]")
assert not is_datetime64_dtype(dtype)
assert not is_datetime64_dtype("datetime64[ns, US/Eastern]")
