# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 15760 UTC=True with Series
ts = 1.5e18
result = to_datetime(Series([ts]), utc=True, cache=cache)
expected = Series([Timestamp(ts, tz="utc")])
tm.assert_series_equal(result, expected)
