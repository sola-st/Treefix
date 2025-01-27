# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
# GH#19036
offset = FY5253Quarter(
    n=-2, qtr_with_extra_week=1, startingMonth=7, variation="last", weekday=2
)
ts = Timestamp("2011-01-26 19:03:40.331096129+0200", tz="Africa/Windhoek")
slow = (ts + offset) - offset == ts
fast = offset.is_on_offset(ts)
assert fast == slow
