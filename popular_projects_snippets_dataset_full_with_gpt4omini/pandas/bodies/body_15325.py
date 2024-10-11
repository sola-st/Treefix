# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = timedelta_range("1 day 10:11:12", freq="h", periods=500)
ser = Series(np.arange(len(rng)), index=rng)

result = ser["5 day":"6 day"]
expected = ser.iloc[86:134]
tm.assert_series_equal(result, expected)

result = ser["5 day":]
expected = ser.iloc[86:]
tm.assert_series_equal(result, expected)

result = ser[:"6 day"]
expected = ser.iloc[:134]
tm.assert_series_equal(result, expected)
