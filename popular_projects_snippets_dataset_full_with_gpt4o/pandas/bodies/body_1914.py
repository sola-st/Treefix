# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
dr = date_range(start="1/1/2012", freq="5min", periods=1000)
s = Series(np.array(100), index=dr)
# subset the data.
subset = s[:"2012-01-04 06:55"]

result = subset.resample("10min").apply(len)
expected = s.resample("10min").apply(len).loc[result.index]
tm.assert_series_equal(result, expected)
