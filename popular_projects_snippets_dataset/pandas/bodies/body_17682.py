# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
# End of long Q1
assert makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(2011, 4, 2))

# Start of long Q1
assert makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(2010, 12, 26))

# End of year before year with long Q1
assert not makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(2010, 12, 25))

for year in [
    x for x in range(1994, 2011 + 1) if x not in [2011, 2005, 2000, 1994]
]:
    assert not makeFY5253LastOfMonthQuarter(
        1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
    ).year_has_extra_week(datetime(year, 4, 2))

# Other long years
assert makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(2005, 4, 2))

assert makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(2000, 4, 2))

assert makeFY5253LastOfMonthQuarter(
    1, startingMonth=12, weekday=WeekDay.SAT, qtr_with_extra_week=1
).year_has_extra_week(datetime(1994, 4, 2))
