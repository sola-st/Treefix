# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 18980
dtype = IntervalDtype(subtype)
assert str(dtype) == "interval"
assert dtype.name == "interval"
