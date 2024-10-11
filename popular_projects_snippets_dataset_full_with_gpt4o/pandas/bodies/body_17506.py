# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
# GH 19036, GH 18977 _adjust_dst was incorrect for LastWeekOfMonth
offset = LastWeekOfMonth(n=n, weekday=weekday)
ts = Timestamp(date, tz=tz)
slow = (ts + offset) - offset == ts
fast = offset.is_on_offset(ts)
assert fast == slow
