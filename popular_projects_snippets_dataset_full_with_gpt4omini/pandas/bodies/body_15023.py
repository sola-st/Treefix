# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py

_, ax = self.plt.subplots()
ax = ts.plot.hist(logy=True, ax=ax)
self._check_ax_scales(ax, yaxis="log")
xlabels = ax.get_xticklabels()
# ticks are values, thus ticklabels are blank
self._check_text_labels(xlabels, [""] * len(xlabels))
ylabels = ax.get_yticklabels()
self._check_text_labels(ylabels, [""] * len(ylabels))

_check_plot_works(ts.plot.kde)
_check_plot_works(ts.plot.density)
_, ax = self.plt.subplots()
ax = ts.plot.kde(logy=True, ax=ax)
self._check_ax_scales(ax, yaxis="log")
xlabels = ax.get_xticklabels()
self._check_text_labels(xlabels, [""] * len(xlabels))
ylabels = ax.get_yticklabels()
self._check_text_labels(ylabels, [""] * len(ylabels))
