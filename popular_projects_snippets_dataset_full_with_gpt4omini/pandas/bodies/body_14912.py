# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# #1890
_, ax = self.plt.subplots()
ax = Series(np.arange(12) + 1, index=date_range("1/1/2000", periods=12)).plot(
    color="green", ax=ax
)
self._check_colors(ax.get_lines(), linecolors=["green"])
