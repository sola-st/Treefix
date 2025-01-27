# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_holiday.py
class TestCalendar(AbstractHolidayCalendar):
    rules = []

calendar = get_calendar("TestCalendar")
assert TestCalendar == type(calendar)
