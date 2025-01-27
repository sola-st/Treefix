# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 18980
closed = "right" if subtype is not None else None
dtype = IntervalDtype(subtype, closed=closed)
expected = f"interval[{subtype}, {closed}]"
assert str(dtype) == expected
assert dtype.name == "interval"
