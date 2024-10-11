# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH1890
_, ax = self.plt.subplots()
ax = Series(np.arange(12) + 1).plot(color="green", ax=ax)
self._check_colors(ax.get_lines(), linecolors=["green"])
