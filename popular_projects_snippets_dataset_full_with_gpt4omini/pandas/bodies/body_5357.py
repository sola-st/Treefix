# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH#13057
ts = Timestamp("2015-11-1 01:00")
msg = "Cannot infer dst time from 2015-11-01 01:00:00,"
with pytest.raises(AmbiguousTimeError, match=msg):
    ts.tz_localize("US/Pacific", ambiguous="raise")
