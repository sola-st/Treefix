# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
ser = Series(
    np.arange(1000000), index=IntervalIndex.from_breaks(np.arange(1000001))
)

result1 = ser.loc[:80000]
result2 = ser.loc[0:80000]
result3 = ser.loc[0:80000:1]
tm.assert_series_equal(result1, result2)
tm.assert_series_equal(result1, result3)
