# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
ts = tm.makeTimeSeries()
grouped = ts.groupby(lambda x: x.month)
result = grouped.apply(lambda x: x.describe())
expected = grouped.describe().stack()
tm.assert_series_equal(result, expected)
