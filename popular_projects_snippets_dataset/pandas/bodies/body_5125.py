# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(10, unit="d")
result = offsets.Hour(1) / td
assert result == 1 / 240.0

assert np.timedelta64(60, "h") / td == 0.25
