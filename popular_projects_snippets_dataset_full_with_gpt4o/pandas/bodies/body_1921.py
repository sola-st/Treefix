# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH2753
timeseries = Series(
    index=pd.bdate_range("20000101", "20000201"), dtype=np.float64
)
res1 = timeseries.resample("BMS").mean()
res2 = timeseries.resample("BMS").mean().resample("B").mean()
assert res1.index[0] == Timestamp("20000103")
assert res1.index[0] == res2.index[0]
