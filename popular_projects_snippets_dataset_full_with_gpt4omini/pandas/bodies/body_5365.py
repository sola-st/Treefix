# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH 8917
tz = warsaw
ts = Timestamp("2015-03-29 02:20:00").as_unit(unit)
msg = "2015-03-29 02:20:00"
with pytest.raises(pytz.NonExistentTimeError, match=msg):
    ts.tz_localize(tz, nonexistent="raise")
msg = (
    "The nonexistent argument must be one of 'raise', 'NaT', "
    "'shift_forward', 'shift_backward' or a timedelta object"
)
with pytest.raises(ValueError, match=msg):
    ts.tz_localize(tz, nonexistent="foo")
