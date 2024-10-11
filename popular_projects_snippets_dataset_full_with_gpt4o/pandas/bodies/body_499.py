# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# generic
i = IntervalDtype(subtype)
assert i.subtype is None
assert is_interval_dtype(i)
