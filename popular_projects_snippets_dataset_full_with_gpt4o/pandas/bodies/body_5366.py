# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
tz = tz_aware_fixture

ts = Timestamp(stamp, tz="UTC")
converted = ts.tz_convert(tz)

reset = converted.tz_convert(None)
assert reset == Timestamp(stamp)
assert reset.tzinfo is None
assert reset == converted.tz_convert("UTC").tz_localize(None)
