# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
date = "20130101 00:00:00"
test_dates = [date] * 10**5
data = Series(test_dates)
result = to_datetime(data, utc=utc, format=format, cache=True)
expected = to_datetime(data, utc=utc, format=format, cache=False)
tm.assert_series_equal(result, expected)
