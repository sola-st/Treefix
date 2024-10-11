# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
# Saturday
last_sat = datetime(2013, 8, 31)
next_sat = datetime(2013, 9, 28)
offset_sat = LastWeekOfMonth(n=1, weekday=5)

one_day_before = last_sat + timedelta(days=-1)
assert one_day_before + offset_sat == last_sat

one_day_after = last_sat + timedelta(days=+1)
assert one_day_after + offset_sat == next_sat

# Test On that day
assert last_sat + offset_sat == next_sat

# Thursday

offset_thur = LastWeekOfMonth(n=1, weekday=3)
last_thurs = datetime(2013, 1, 31)
next_thurs = datetime(2013, 2, 28)

one_day_before = last_thurs + timedelta(days=-1)
assert one_day_before + offset_thur == last_thurs

one_day_after = last_thurs + timedelta(days=+1)
assert one_day_after + offset_thur == next_thurs

# Test on that day
assert last_thurs + offset_thur == next_thurs

three_before = last_thurs + timedelta(days=-3)
assert three_before + offset_thur == last_thurs

two_after = last_thurs + timedelta(days=+2)
assert two_after + offset_thur == next_thurs

offset_sunday = LastWeekOfMonth(n=1, weekday=WeekDay.SUN)
assert datetime(2013, 7, 31) + offset_sunday == datetime(2013, 8, 25)
