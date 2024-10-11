# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
_, ax = self.plt.subplots()
ax = ts.plot.box(logy=True, ax=ax)
self._check_ax_scales(ax, yaxis="log")
xlabels = ax.get_xticklabels()
self._check_text_labels(xlabels, [ts.name])
ylabels = ax.get_yticklabels()
self._check_text_labels(ylabels, [""] * len(ylabels))
