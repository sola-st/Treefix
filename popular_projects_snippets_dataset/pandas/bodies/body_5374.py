# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH21358
tz = timezones.maybe_get_tz(tz_naive_fixture)

stamp = Timestamp("2018-06-04 10:20:30", tz=tz)
_datetime = datetime(2018, 6, 4, hour=10, minute=20, second=30, tzinfo=tz)

result = stamp.timetz()
expected = _datetime.timetz()

assert result == expected
