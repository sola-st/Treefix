# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
i = IntervalDtype(subtype, closed="right")
assert i.subtype == np.dtype("int64")
assert is_interval_dtype(i)
