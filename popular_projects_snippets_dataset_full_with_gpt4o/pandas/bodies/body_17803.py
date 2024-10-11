# Extracted from ./data/repos/pandas/pandas/tests/tseries/holiday/test_holiday.py
assert list(holiday.dates(start_date, end_date)) == expected

# Verify that timezone info is preserved.
assert list(
    holiday.dates(
        utc.localize(Timestamp(start_date)), utc.localize(Timestamp(end_date))
    )
) == [utc.localize(dt) for dt in expected]
