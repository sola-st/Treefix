# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH#13057
ts = Timestamp(stamp)
with pytest.raises(NonExistentTimeError, match=stamp):
    ts.tz_localize(tz)
# GH 22644
with pytest.raises(NonExistentTimeError, match=stamp):
    ts.tz_localize(tz, nonexistent="raise")
assert ts.tz_localize(tz, nonexistent="NaT") is NaT
