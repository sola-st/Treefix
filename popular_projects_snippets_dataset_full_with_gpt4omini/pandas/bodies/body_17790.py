# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_calendar.py
us_fed_cal = get_calendar("USFederalHolidayCalendar")
assert us_fed_cal.rule_from_name("Thanksgiving Day") == USThanksgivingDay
