# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

ts = pd.date_range("20130101", periods=3)
tsa = pd.date_range("20130101", periods=3, tz="US/Eastern")

assert is_datetime64_dtype("datetime64")
assert is_datetime64_dtype("datetime64[ns]")
assert is_datetime64_dtype(ts)
assert not is_datetime64_dtype(tsa)

assert not is_datetime64_ns_dtype("datetime64")
assert is_datetime64_ns_dtype("datetime64[ns]")
assert is_datetime64_ns_dtype(ts)
assert is_datetime64_ns_dtype(tsa)

assert is_datetime64_any_dtype("datetime64")
assert is_datetime64_any_dtype("datetime64[ns]")
assert is_datetime64_any_dtype(ts)
assert is_datetime64_any_dtype(tsa)

assert not is_datetime64tz_dtype("datetime64")
assert not is_datetime64tz_dtype("datetime64[ns]")
assert not is_datetime64tz_dtype(ts)
assert is_datetime64tz_dtype(tsa)
