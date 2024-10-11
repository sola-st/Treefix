# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(10, unit="d")

result = td / offsets.Hour(1)
assert result == 240

assert td / td == 1
assert td / np.timedelta64(60, "h") == 4

assert np.isnan(td / NaT)
