# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
offset = makeFY5253NearestEndMonthQuarter(
    1, startingMonth=8, weekday=WeekDay.THU, qtr_with_extra_week=4
)

MU = [
    datetime(2012, 5, 31),
    datetime(2012, 8, 30),
    datetime(2012, 11, 29),
    datetime(2013, 2, 28),
    datetime(2013, 5, 30),
]

date = MU[0] + relativedelta(days=-1)
for expected in MU:
    assert_offset_equal(offset, date, expected)
    date = date + offset

assert_offset_equal(offset, datetime(2012, 5, 31), datetime(2012, 8, 30))
assert_offset_equal(offset, datetime(2012, 5, 30), datetime(2012, 5, 31))

offset2 = FY5253Quarter(
    weekday=5, startingMonth=12, variation="last", qtr_with_extra_week=4
)

assert_offset_equal(offset2, datetime(2013, 1, 15), datetime(2013, 3, 30))
