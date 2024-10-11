# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
offset = makeFY5253LastOfMonthQuarter(
    1, startingMonth=9, weekday=WeekDay.SAT, qtr_with_extra_week=4
)
offset2 = makeFY5253LastOfMonthQuarter(
    2, startingMonth=9, weekday=WeekDay.SAT, qtr_with_extra_week=4
)
offset4 = makeFY5253LastOfMonthQuarter(
    4, startingMonth=9, weekday=WeekDay.SAT, qtr_with_extra_week=4
)

offset_neg1 = makeFY5253LastOfMonthQuarter(
    -1, startingMonth=9, weekday=WeekDay.SAT, qtr_with_extra_week=4
)
offset_neg2 = makeFY5253LastOfMonthQuarter(
    -2, startingMonth=9, weekday=WeekDay.SAT, qtr_with_extra_week=4
)

GMCR = [
    datetime(2010, 3, 27),
    datetime(2010, 6, 26),
    datetime(2010, 9, 25),
    datetime(2010, 12, 25),
    datetime(2011, 3, 26),
    datetime(2011, 6, 25),
    datetime(2011, 9, 24),
    datetime(2011, 12, 24),
    datetime(2012, 3, 24),
    datetime(2012, 6, 23),
    datetime(2012, 9, 29),
    datetime(2012, 12, 29),
    datetime(2013, 3, 30),
    datetime(2013, 6, 29),
]

assert_offset_equal(offset, base=GMCR[0], expected=GMCR[1])
assert_offset_equal(
    offset, base=GMCR[0] + relativedelta(days=-1), expected=GMCR[0]
)
assert_offset_equal(offset, base=GMCR[1], expected=GMCR[2])

assert_offset_equal(offset2, base=GMCR[0], expected=GMCR[2])
assert_offset_equal(offset4, base=GMCR[0], expected=GMCR[4])

assert_offset_equal(offset_neg1, base=GMCR[-1], expected=GMCR[-2])
assert_offset_equal(
    offset_neg1, base=GMCR[-1] + relativedelta(days=+1), expected=GMCR[-1]
)
assert_offset_equal(offset_neg2, base=GMCR[-1], expected=GMCR[-3])

date = GMCR[0] + relativedelta(days=-1)
for expected in GMCR:
    assert_offset_equal(offset, date, expected)
    date = date + offset

date = GMCR[-1] + relativedelta(days=+1)
for expected in reversed(GMCR):
    assert_offset_equal(offset_neg1, date, expected)
    date = date + offset_neg1
