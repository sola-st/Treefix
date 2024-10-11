# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
ts_ind = date_range("2012-01-01 13:00", "2012-01-02", freq="H")
ts_data = np.random.randn(12)

ts = Series(ts_data, index=ts_ind)
ts2 = ts.asfreq("T").interpolate()

_, ax = self.plt.subplots()
ax = ts.plot(ax=ax)
ts2.plot(style="r", ax=ax)

assert ax.lines[0].get_xdata()[0] == ax.lines[1].get_xdata()[0]
