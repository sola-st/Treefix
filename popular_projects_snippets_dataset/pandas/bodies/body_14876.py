# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# figsize and title
_, ax = self.plt.subplots()
ax = series.plot(title="Test", figsize=(16, 8), ax=ax)
self._check_text_labels(ax.title, "Test")
self._check_axes_shape(ax, axes_num=1, layout=(1, 1), figsize=(16, 8))
