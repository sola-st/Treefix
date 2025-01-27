# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 31043
# Make sure that calling Timestamp constructor
# on time just before DST switch doesn't lead to
# nonexistent time or value change
ts = Timestamp(epoch, tz="dateutil/America/Los_Angeles")
result = ts.tz.dst(ts)
expected = timedelta(seconds=0)
assert Timestamp(ts).value == epoch
assert result == expected
