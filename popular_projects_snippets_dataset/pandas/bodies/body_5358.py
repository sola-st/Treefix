# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH 22644
tz = warsaw
ts = Timestamp("2015-03-29 02:00:00")
msg = (
    "The nonexistent argument must be one of 'raise', 'NaT', "
    "'shift_forward', 'shift_backward' or a timedelta object"
)
with pytest.raises(ValueError, match=msg):
    ts.tz_localize(tz, nonexistent="foo")
