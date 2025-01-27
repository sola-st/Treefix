# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
dtype = f"datetime64[ns, {tz}]"
assert not is_datetime64_dtype(dtype)
assert is_datetime64tz_dtype(dtype)
assert is_datetime64_ns_dtype(dtype)
assert is_datetime64_any_dtype(dtype)
