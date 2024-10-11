# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = DataFrame(np.random.randn(10, 2))
_, ax = self.plt.subplots()
ax = df.plot.hist(bins=5, ax=ax)
assert len(ax.patches) == 10
