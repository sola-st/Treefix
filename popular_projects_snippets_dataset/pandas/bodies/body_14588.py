# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
bts = tm.makePeriodSeries()
_, ax = self.plt.subplots()
bts.plot(ax=ax)
assert ax.get_lines()[0].get_xydata()[0, 0] == bts.index[0].ordinal
idx = ax.get_lines()[0].get_xdata()
assert PeriodIndex(data=idx).freqstr == "B"
