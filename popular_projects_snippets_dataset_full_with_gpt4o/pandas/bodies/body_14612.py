# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
s1 = tm.makeTimeSeries()
s2 = s1[[0, 5, 10, 11, 12, 13, 14, 15]]
_, ax = self.plt.subplots()
s2.plot(style="g", ax=ax)
s1.plot(ax=ax)
assert not hasattr(ax, "freq")
lines = ax.get_lines()
x1 = lines[0].get_xdata()
tm.assert_numpy_array_equal(x1, s2.index.astype(object).values)
x2 = lines[1].get_xdata()
tm.assert_numpy_array_equal(x2, s1.index.astype(object).values)
