# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
alt = Timestamp(dt64)

assert ts.year == alt.year
assert ts.month == alt.month
assert ts.day == alt.day
assert ts.hour == ts.minute == ts.second == ts.microsecond == 0
assert ts.nanosecond == 0

assert ts.to_julian_date() == alt.to_julian_date()
assert ts.weekday() == alt.weekday()
assert ts.isoweekday() == alt.isoweekday()
