# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert DateOffset(2) == 2 * DateOffset(1)
assert DateOffset(2) == DateOffset(1) * 2
