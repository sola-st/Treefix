# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 9852
s1 = tm.makeTimeSeries().to_frame()
s2 = s1.iloc[[0, 5, 10, 11, 12, 13, 14, 15], :]
_, ax = self.plt.subplots()
s1.plot(ax=ax)
ax2 = s2.plot(style="g", ax=ax)
lines = ax2.get_lines()
idx1 = PeriodIndex(lines[0].get_xdata())
idx2 = PeriodIndex(lines[1].get_xdata())
assert idx1.equals(s1.index.to_period("B"))
assert idx2.equals(s2.index.to_period("B"))
left, right = ax2.get_xlim()
pidx = s1.index.to_period()
assert left <= pidx[0].ordinal
assert right >= pidx[-1].ordinal
