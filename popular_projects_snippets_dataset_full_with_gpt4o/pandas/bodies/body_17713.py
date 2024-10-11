# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_ticks.py
result = offsets.Hour(3) + offsets.Hour(4)
exp = offsets.Hour(7)
assert result == exp
