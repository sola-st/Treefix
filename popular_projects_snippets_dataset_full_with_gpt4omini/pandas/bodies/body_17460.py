# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert DateOffset(months=2).copy() == DateOffset(months=2)
assert DateOffset(milliseconds=1).copy() == DateOffset(milliseconds=1)
