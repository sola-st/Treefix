# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
# GH 18510 Week with weekday = None, normalize = False
# should always be is_on_offset
offset = Week(n=n, weekday=None)
ts = Timestamp(date, tz="Africa/Lusaka")
fast = offset.is_on_offset(ts)
slow = (ts + offset) - offset == ts
assert fast == slow
