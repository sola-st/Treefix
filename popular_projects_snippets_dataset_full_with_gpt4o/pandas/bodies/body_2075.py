# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 32792
dates = [
    "2010-01-01 12:00:00 +0100",
    "2010-01-01 12:00:00 -0100",
    "2010-01-01 12:00:00 +0300",
    "2010-01-01 12:00:00 +0400",
]
expected_dates = [
    "2010-01-01 11:00:00+00:00",
    "2010-01-01 13:00:00+00:00",
    "2010-01-01 09:00:00+00:00",
    "2010-01-01 08:00:00+00:00",
]
fmt = "%Y-%m-%d %H:%M:%S %z"

result = to_datetime(dates, format=fmt, utc=True)
expected = DatetimeIndex(expected_dates)
tm.assert_index_equal(result, expected)
