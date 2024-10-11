# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# March 13, 2011, spring forward, skip from 2 AM to 3 AM
dr = date_range(datetime(2011, 3, 13, 1, 30), periods=3, freq=pd.offsets.Hour())
with pytest.raises(pytz.NonExistentTimeError, match="2011-03-13 02:30:00"):
    dr.tz_localize(tz)

# after dst transition, it works
dr = date_range(
    datetime(2011, 3, 13, 3, 30), periods=3, freq=pd.offsets.Hour(), tz=tz
)

# November 6, 2011, fall back, repeat 2 AM hour
dr = date_range(datetime(2011, 11, 6, 1, 30), periods=3, freq=pd.offsets.Hour())
with pytest.raises(pytz.AmbiguousTimeError, match="Cannot infer dst time"):
    dr.tz_localize(tz)

# UTC is OK
dr = date_range(
    datetime(2011, 3, 13), periods=48, freq=pd.offsets.Minute(30), tz=pytz.utc
)
