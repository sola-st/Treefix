# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
d = [datetime(2012, 8, 19, tzinfo=tz)]

index = DatetimeIndex(d)
assert timezones.tz_compare(index.tz, tz)
