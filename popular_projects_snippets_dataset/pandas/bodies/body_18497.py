# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
# see gh-13583
tz = timezones.maybe_get_tz("tzlocal()")
assert tz == dateutil.tz.tzlocal()
