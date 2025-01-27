# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# #1465
s = Series(
    np.random.randn(21),
    index=date_range(start="1/1/2012 9:30", freq="1min", periods=21),
)
s[0] = np.nan

result = s.resample("10min", closed="left", label="right").mean()
exp = s[1:].resample("10min", closed="left", label="right").mean()
tm.assert_series_equal(result, exp)

result = s.resample("10min", closed="left", label="left").mean()
exp = s[1:].resample("10min", closed="left", label="left").mean()

ex_index = date_range(start="1/1/2012 9:30", freq="10min", periods=3)

tm.assert_index_equal(result.index, ex_index)
tm.assert_series_equal(result, exp)
