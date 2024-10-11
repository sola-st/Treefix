# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert not is_datetime64_ns_dtype(dtype)
assert not is_datetime64_ns_dtype("period[D]")
assert not is_datetime64_dtype(dtype)
assert not is_datetime64_dtype("period[D]")
