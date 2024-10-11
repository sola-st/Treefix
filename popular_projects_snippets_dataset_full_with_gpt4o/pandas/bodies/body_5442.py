# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
stamp = Timestamp("20090415", tz="dateutil/US/Eastern")
dtval = stamp.to_pydatetime()
assert stamp == dtval
assert stamp.tzinfo == dtval.tzinfo
