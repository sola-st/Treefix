# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH#38394
dtype = IntervalDtype(subtype)

assert dtype.closed is None
