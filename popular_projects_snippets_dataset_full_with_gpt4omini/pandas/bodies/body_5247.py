# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH#21344
td = Timedelta(days=4, hours=3)
result = td.resolution
assert result == Timedelta(nanoseconds=1)

# Check that the attribute is available on the class, mirroring
#  the stdlib timedelta behavior
result = Timedelta.resolution
assert result == Timedelta(nanoseconds=1)
