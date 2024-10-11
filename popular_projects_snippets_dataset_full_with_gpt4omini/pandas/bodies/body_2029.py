# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# Series
expected = Series([timedelta(days=1), timedelta(days=1, seconds=1)])
result = to_timedelta(Series(["1d", "1days 00:00:01"]))
tm.assert_series_equal(result, expected)
