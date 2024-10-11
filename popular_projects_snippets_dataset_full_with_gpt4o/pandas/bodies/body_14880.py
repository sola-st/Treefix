# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH37942
fig, (ax1, ax2) = self.plt.subplots(1, 2, sharey=True)

abs(ts).plot(ax=ax1, kind="area")
abs(ts).plot(ax=ax2, kind="area")

assert self.get_y_axis(ax1).joined(ax1, ax2)
assert self.get_y_axis(ax2).joined(ax1, ax2)
