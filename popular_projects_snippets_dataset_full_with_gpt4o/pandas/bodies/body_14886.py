# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
df = Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
_, ax = self.plt.subplots()
ax = df.plot.bar(use_index=False, ax=ax)
self._check_text_labels(ax.get_xticklabels(), ["0", "1", "2", "3"])
