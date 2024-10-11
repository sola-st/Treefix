# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
oset = offsets.DateOffset(months=2, days=4)
# it works
oset.freqstr

assert not offsets.DateOffset(months=2) == 2
