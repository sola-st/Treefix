# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
tz = timezones.maybe_get_tz(utc_fixture)
tz2 = timezones.maybe_get_tz(utc_fixture2)
assert timezones.tz_compare(tz, tz2)
