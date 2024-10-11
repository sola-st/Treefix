# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#14956
series = Series([datetime(2015, 1, 1, tzinfo=pytz.utc), 1])
result = series.ffill()
tm.assert_series_equal(series, result)
