# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
utc_stamp = Timestamp("3/11/2012 05:00", tz="utc")
assert utc_stamp.tzinfo is timezone.utc
assert utc_stamp.hour == 5

utc_stamp = Timestamp("3/11/2012 05:00").tz_localize("utc")
assert utc_stamp.hour == 5
