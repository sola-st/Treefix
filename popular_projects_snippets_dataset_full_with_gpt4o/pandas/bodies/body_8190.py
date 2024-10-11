# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH 8917
tz = warsaw
dti = DatetimeIndex([Timestamp("2015-03-29 02:20:00")])
msg = "The provided timedelta will relocalize on a nonexistent time"
with pytest.raises(ValueError, match=msg):
    dti.tz_localize(tz, nonexistent=timedelta(seconds=offset))
