# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
assert is_interval_dtype("interval[int64, both]")
assert is_interval_dtype(IntervalIndex.from_tuples([(0, 1)]))
assert is_interval_dtype(IntervalIndex.from_breaks(np.arange(4)))
assert is_interval_dtype(
    IntervalIndex.from_breaks(date_range("20130101", periods=3))
)
assert not is_interval_dtype("U")
assert not is_interval_dtype("S")
assert not is_interval_dtype("foo")
assert not is_interval_dtype(np.object_)
assert not is_interval_dtype(np.int64)
assert not is_interval_dtype(np.float64)
