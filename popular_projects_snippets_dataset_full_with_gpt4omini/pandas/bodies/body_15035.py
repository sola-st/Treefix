# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 9853
with tm.RNGContext(1):
    df = DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df["E"] = ["x", "y"] * 5
_, ax = self.plt.subplots()
ax = df.plot.hist(bins=5, ax=ax)
assert len(ax.patches) == 20

_, ax = self.plt.subplots()
ax = df.plot.hist(ax=ax)  # bins=10
assert len(ax.patches) == 40
