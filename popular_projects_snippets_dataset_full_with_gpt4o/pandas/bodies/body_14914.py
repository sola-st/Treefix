# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH11529
s = Series(np.arange(10), index=[f"P{i:02d}" for i in range(10)])
_, ax = self.plt.subplots()
ax = s.plot(xticks=[0, 3, 5, 9], ax=ax)
exp = [f"P{i:02d}" for i in [0, 3, 5, 9]]
self._check_text_labels(ax.get_xticklabels(), exp)
