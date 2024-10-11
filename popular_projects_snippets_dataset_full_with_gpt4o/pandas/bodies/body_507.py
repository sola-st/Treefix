# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
a = IntervalDtype("interval[int64, right]")
b = IntervalDtype("interval[int64, right]")

assert issubclass(type(a), type(a))
assert issubclass(type(a), type(b))
