# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
ts = tm.makeTimeSeries()
_, ax = self.plt.subplots()
ts.plot(style="k", ax=ax)
color = (0.0, 0.0, 0.0, 1)
assert color == ax.get_lines()[0].get_color()
