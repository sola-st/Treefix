# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
assert offsets.Hour(1) // Timedelta(minutes=25) == 2
