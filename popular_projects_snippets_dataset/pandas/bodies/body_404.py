# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_interval_dtype(object)
assert not com.is_interval_dtype([1, 2, 3])

assert com.is_interval_dtype(IntervalDtype())

interval = pd.Interval(1, 2, closed="right")
assert not com.is_interval_dtype(interval)
assert com.is_interval_dtype(pd.IntervalIndex([interval]))
