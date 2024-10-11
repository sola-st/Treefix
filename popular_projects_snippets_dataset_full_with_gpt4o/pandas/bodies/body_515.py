# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
IntervalDtype.reset_cache()
dtype = IntervalDtype("int64", "right")
assert len(IntervalDtype._cache_dtypes) == 1

IntervalDtype("interval")
assert len(IntervalDtype._cache_dtypes) == 2

IntervalDtype.reset_cache()
tm.round_trip_pickle(dtype)
assert len(IntervalDtype._cache_dtypes) == 0
