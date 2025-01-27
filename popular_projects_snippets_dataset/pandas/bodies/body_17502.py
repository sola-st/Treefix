# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
# GH 18864
# Make sure that nanoseconds don't trip up is_on_offset (and with it apply)
offset = WeekOfMonth(n=n, week=week, weekday=0)
ts = Timestamp(date, tz=tz)
fast = offset.is_on_offset(ts)
slow = (ts + offset) - offset == ts
assert fast == slow
