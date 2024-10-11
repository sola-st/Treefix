# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#49737
ts = Timestamp("2016-01-01 04:05:06-01:00")
assert ts.unit == "s"

ts = Timestamp("2016-01-01 04:05:06.000-01:00")
assert ts.unit == "ms"

ts = Timestamp("2016-01-01 04:05:06.000000-01:00")
assert ts.unit == "us"

ts = Timestamp("2016-01-01 04:05:06.000000001-01:00")
assert ts.unit == "ns"
