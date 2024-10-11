# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_timedelta64_ns_dtype(np.dtype("m8[ps]"))
assert not com.is_timedelta64_ns_dtype(np.array([1, 2], dtype=np.timedelta64))

assert com.is_timedelta64_ns_dtype(np.dtype("m8[ns]"))
assert com.is_timedelta64_ns_dtype(np.array([1, 2], dtype="m8[ns]"))
