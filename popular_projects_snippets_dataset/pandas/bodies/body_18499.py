# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
# even if the machine running the test is localized to UTC
tz = dateutil.tz.tzlocal()
assert not timezones.is_utc(tz)

assert not timezones.tz_compare(tz, dateutil.tz.tzutc())
