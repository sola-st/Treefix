# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# higher reso
rng = timedelta_range("1 day 10:11:12", freq="us", periods=2000)
ser = Series(np.arange(len(rng)), index=rng)

result = ser["1 day 10:11:12":]
expected = ser.iloc[0:]
tm.assert_series_equal(result, expected)

result = ser["1 day 10:11:12.001":]
expected = ser.iloc[1000:]
tm.assert_series_equal(result, expected)

result = ser["1 days, 10:11:12.001001"]
assert result == ser.iloc[1001]
