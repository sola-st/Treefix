# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
assert makeFY5253LastOfMonthQuarter(
    startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4
) == makeFY5253LastOfMonthQuarter(
    startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4
)
assert makeFY5253LastOfMonthQuarter(
    startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4
) != makeFY5253LastOfMonthQuarter(
    startingMonth=1, weekday=WeekDay.SUN, qtr_with_extra_week=4
)
assert makeFY5253LastOfMonthQuarter(
    startingMonth=1, weekday=WeekDay.SAT, qtr_with_extra_week=4
) != makeFY5253LastOfMonthQuarter(
    startingMonth=2, weekday=WeekDay.SAT, qtr_with_extra_week=4
)
