# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 25959
# Calling apply on a localized time series should not cause an error
series = tm.makeTimeSeries(nper=30).tz_localize("UTC")
result = Series(series.index).apply(lambda x: 1)
tm.assert_series_equal(result, Series(np.ones(30), dtype="int64"))
