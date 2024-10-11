# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_federal.py
class MemorialDay(AbstractHolidayCalendar):
    rules = [USMemorialDay]

holidays = MemorialDay().holidays(start="1971", end="1980").to_pydatetime().tolist()

# Fixes 5/31 error and checked manually against Wikipedia.
assert holidays == [
    datetime(1971, 5, 31, 0, 0),
    datetime(1972, 5, 29, 0, 0),
    datetime(1973, 5, 28, 0, 0),
    datetime(1974, 5, 27, 0, 0),
    datetime(1975, 5, 26, 0, 0),
    datetime(1976, 5, 31, 0, 0),
    datetime(1977, 5, 30, 0, 0),
    datetime(1978, 5, 29, 0, 0),
    datetime(1979, 5, 28, 0, 0),
]
