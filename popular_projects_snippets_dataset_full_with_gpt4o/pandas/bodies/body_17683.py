# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
sat_dec_1 = makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
)
sat_dec_4 = makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=4
)

assert sat_dec_1.get_weeks(datetime(2011, 4, 2)) == [14, 13, 13, 13]
assert sat_dec_4.get_weeks(datetime(2011, 4, 2)) == [13, 13, 13, 14]
assert sat_dec_1.get_weeks(datetime(2010, 12, 25)) == [13, 13, 13, 13]
