# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
bts = DataFrame({"a": tm.makeTimeSeries()})
_, ax = self.plt.subplots()
bts.plot(ax=ax)
idx = ax.get_lines()[0].get_xdata()
tm.assert_index_equal(bts.index.to_period(), PeriodIndex(idx))
