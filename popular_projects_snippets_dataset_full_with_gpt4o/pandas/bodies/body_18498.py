# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
# see gh-13583
#
# Get offset using normal datetime for test.
ts = Timestamp("2011-01-01", tz=dateutil.tz.tzlocal())

offset = dateutil.tz.tzlocal().utcoffset(datetime(2011, 1, 1))
offset = offset.total_seconds()

assert ts.value + offset == Timestamp("2011-01-01").value
