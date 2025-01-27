# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 19974
index = date_range(start="2018", freq="M", periods=6)
data = np.ones(6)
data[3:6] = np.nan
s = Series(data, index).to_period()
result = s.resample("Q").sum(min_count=1)
expected = Series(
    [3.0, np.nan], index=PeriodIndex(["2018Q1", "2018Q2"], freq="Q-DEC")
)
tm.assert_series_equal(result, expected)
