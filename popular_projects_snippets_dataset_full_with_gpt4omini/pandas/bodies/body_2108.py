# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
expected = Series([Timestamp("2013-01-01 01:00:00", tz="UTC")])
result = to_datetime(Series([date], dtype=dtype), utc=True, cache=cache)
tm.assert_series_equal(result, expected)
