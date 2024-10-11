# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
ts = tm.makeTimeSeries()
irreg = ts[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 29]]
rng = period_range("1/3/2000", periods=30, freq="B")
ps = Series(np.random.randn(len(rng)), rng)
_, ax = self.plt.subplots()
irreg.plot(ax=ax)
ps.plot(ax=ax)
