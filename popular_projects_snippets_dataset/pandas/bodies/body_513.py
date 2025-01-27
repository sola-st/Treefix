# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_interval_dtype(dtype)

ii = IntervalIndex.from_breaks(range(3))

assert is_interval_dtype(ii.dtype)
assert is_interval_dtype(ii)

s = Series(ii, name="A")

assert is_interval_dtype(s.dtype)
assert is_interval_dtype(s)
