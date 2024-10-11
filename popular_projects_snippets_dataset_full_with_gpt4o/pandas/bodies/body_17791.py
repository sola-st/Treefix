# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_calendar.py
# See gh-27790
#
# Labor Day 2031 is on September 1. Saturday before is August 30.
# Next working day after August 30 ought to be Tuesday, September 2.

class testCalendar(AbstractHolidayCalendar):
    rules = [USLaborDay]

cal = testCalendar()
workDay = offsets.CustomBusinessDay(calendar=cal)
Sat_before_Labor_Day_2031 = to_datetime("2031-08-30")
next_working_day = Sat_before_Labor_Day_2031 + 0 * workDay
assert next_working_day == to_datetime("2031-09-02")
