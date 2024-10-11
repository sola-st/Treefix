# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ts = "2013-01-01 00:00:00-01:00"
expected_ts = "2013-01-01 01:00:00"
data = Series([ts] * 3)
result = to_datetime(data, utc=True, cache=cache)
expected = Series([Timestamp(expected_ts, tz="utc")] * 3)
tm.assert_series_equal(result, expected)
