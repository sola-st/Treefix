# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
tz = timezones.maybe_get_tz(utc_fixture)
assert timezones.is_utc(tz)
