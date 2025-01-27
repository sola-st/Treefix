# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
df = DataFrame(np.random.randn(10, 2))
ax = df.hist(bins=2)[0][0]
assert len(ax.patches) == 2
