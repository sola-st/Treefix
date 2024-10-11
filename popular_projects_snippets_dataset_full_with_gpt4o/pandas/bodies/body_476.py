# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py

assert is_datetime64tz_dtype(dtype)

dr = date_range("20130101", periods=3, tz="US/Eastern")
s = Series(dr, name="A")

# dtypes
assert is_datetime64tz_dtype(s.dtype)
assert is_datetime64tz_dtype(s)
assert not is_datetime64tz_dtype(np.dtype("float64"))
assert not is_datetime64tz_dtype(1.0)
