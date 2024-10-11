# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_calendar.py
# see gh-9552.

class TestCalendar(AbstractHolidayCalendar):
    def __init__(self, name=None, rules=None) -> None:
        super().__init__(name=name, rules=rules)

jan1 = TestCalendar(rules=[Holiday("jan1", year=2015, month=1, day=1)])
jan2 = TestCalendar(rules=[Holiday("jan2", year=2015, month=1, day=2)])

# Getting holidays for Jan 1 should not alter results for Jan 2.
tm.assert_index_equal(jan1.holidays(), DatetimeIndex(["01-Jan-2015"]))
tm.assert_index_equal(jan2.holidays(), DatetimeIndex(["02-Jan-2015"]))
