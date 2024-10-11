# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
ts = tm.makeTimeSeries()
grouped = ts.groupby([lambda x: x.year, lambda x: x.month])

result = grouped.agg(np.sum)
expected = grouped.sum()
tm.assert_series_equal(result, expected)
