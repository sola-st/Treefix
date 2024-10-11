# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert is_timedelta64_dtype("timedelta64")
assert is_timedelta64_dtype("timedelta64[ns]")
assert not is_timedelta64_ns_dtype("timedelta64")
assert is_timedelta64_ns_dtype("timedelta64[ns]")

tdi = TimedeltaIndex([1e14, 2e14], dtype="timedelta64[ns]")
assert is_timedelta64_dtype(tdi)
assert is_timedelta64_ns_dtype(tdi)
assert is_timedelta64_ns_dtype(tdi.astype("timedelta64[ns]"))

assert not is_timedelta64_ns_dtype(Index([], dtype=np.float64))
assert not is_timedelta64_ns_dtype(Index([], dtype=np.int64))
