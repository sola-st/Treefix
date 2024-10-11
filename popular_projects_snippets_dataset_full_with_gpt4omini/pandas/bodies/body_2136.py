# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
from pandas.tests.indexes.datetimes.test_timezones import fixed_off

dates = [
    datetime(2000, 1, 1, tzinfo=fixed_off),
    datetime(2000, 1, 2, tzinfo=fixed_off),
    datetime(2000, 1, 3, tzinfo=fixed_off),
]
result = to_datetime(dates)
assert result.tz == fixed_off
