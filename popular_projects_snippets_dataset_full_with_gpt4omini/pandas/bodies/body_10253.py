# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 32108
periods = 2
index = pd.period_range(
    start="2018-01", periods=periods, freq="M", name="Month"
)
period_series = Series(range(periods), index=index)
result = period_series.groupby(period_series.index.month).sum()

expected = Series(
    range(0, periods), index=Index(range(1, periods + 1), name=index.name)
)
tm.assert_series_equal(result, expected)
