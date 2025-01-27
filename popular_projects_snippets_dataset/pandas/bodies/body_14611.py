# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# TODO
s1 = tm.makeTimeSeries()
s2 = s1[[0, 5, 10, 11, 12, 13, 14, 15]]

# it works!
_, ax = self.plt.subplots()
s1.plot(ax=ax)

ax2 = s2.plot(style="g", ax=ax)
lines = ax2.get_lines()
idx1 = PeriodIndex(lines[0].get_xdata())
idx2 = PeriodIndex(lines[1].get_xdata())

tm.assert_index_equal(idx1, s1.index.to_period("B"))
tm.assert_index_equal(idx2, s2.index.to_period("B"))

left, right = ax2.get_xlim()
pidx = s1.index.to_period()
assert left <= pidx[0].ordinal
assert right >= pidx[-1].ordinal
