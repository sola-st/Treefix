# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH 8917
tz = warsaw
ts = Timestamp("2015-03-29 02:20:00").as_unit(unit)
result = ts.tz_localize(tz, nonexistent="NaT")
assert result is NaT
