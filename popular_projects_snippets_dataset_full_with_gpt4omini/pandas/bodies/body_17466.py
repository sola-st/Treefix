# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset1 = DateOffset(days=1)
offset2 = DateOffset(days=365)

assert offset1 != offset2

assert DateOffset(milliseconds=3) != DateOffset(milliseconds=7)
