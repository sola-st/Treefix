# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH#2993, Timestamp cannot be constructed by datetime.date
# and tz correctly

result = Timestamp(date(2012, 3, 11), tz=tz)

expected = Timestamp("3/11/2012", tz=tz)
assert result.hour == expected.hour
assert result == expected
