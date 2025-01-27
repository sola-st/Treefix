# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(hours=3, minutes=4)
assert td // offsets.Hour(1) == 3
assert td // offsets.Minute(2) == 92
