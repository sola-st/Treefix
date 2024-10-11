# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# make sure that we satisfy is semantics
dtype2 = IntervalDtype("int64", "right")
dtype3 = IntervalDtype(dtype2)
assert dtype == dtype2
assert dtype2 == dtype
assert dtype3 == dtype
assert dtype is dtype2
assert dtype2 is dtype3
assert dtype3 is dtype
assert hash(dtype) == hash(dtype2)
assert hash(dtype) == hash(dtype3)

dtype1 = IntervalDtype("interval")
dtype2 = IntervalDtype(dtype1)
dtype3 = IntervalDtype("interval")
assert dtype2 == dtype1
assert dtype2 == dtype2
assert dtype2 == dtype3
assert dtype2 is dtype1
assert dtype2 is dtype2
assert dtype2 is dtype3
assert hash(dtype2) == hash(dtype1)
assert hash(dtype2) == hash(dtype2)
assert hash(dtype2) == hash(dtype3)
