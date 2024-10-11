# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH#21336, GH#21365
dt = Timestamp("2100-01-01 00:00:00.000000000")
assert dt.resolution == Timedelta(nanoseconds=1)

# Check that the attribute is available on the class, mirroring
#  the stdlib datetime behavior
assert Timestamp.resolution == Timedelta(nanoseconds=1)

assert dt.as_unit("us").resolution == Timedelta(microseconds=1)
assert dt.as_unit("ms").resolution == Timedelta(milliseconds=1)
assert dt.as_unit("s").resolution == Timedelta(seconds=1)
