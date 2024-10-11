# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH 8917, 24466
tz = warsaw
ts = Timestamp("2015-03-29 02:20:00")
msg = "The provided timedelta will relocalize on a nonexistent time"
with pytest.raises(ValueError, match=msg):
    ts.tz_localize(tz, nonexistent=timedelta(seconds=offset))
