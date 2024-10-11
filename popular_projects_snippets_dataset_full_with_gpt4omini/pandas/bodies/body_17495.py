# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
offset = Week(weekday=weekday)

for day in range(1, 8):
    date = datetime(2008, 1, day)
    expected = day % 7 == weekday
assert_is_on_offset(offset, date, expected)
