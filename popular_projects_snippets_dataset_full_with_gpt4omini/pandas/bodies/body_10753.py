# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
ts = tm.makeTimeSeries()
grouped = ts.groupby([lambda x: x.year, lambda x: x.month])
result = grouped.describe()
tm.assert_series_equal(result["mean"], grouped.mean(), check_names=False)
tm.assert_series_equal(result["std"], grouped.std(), check_names=False)
tm.assert_series_equal(result["min"], grouped.min(), check_names=False)
