# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# it works!
index = DatetimeIndex([datetime(2012, 1, 1)], tz=prefix + "EST")
index.hour
index[0]
