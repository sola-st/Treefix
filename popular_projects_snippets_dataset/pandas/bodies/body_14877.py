# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 8242
key = "axes.prop_cycle"
colors = self.plt.rcParams[key]
_, ax = self.plt.subplots()
Series([1, 2, 3]).plot(ax=ax)
assert colors == self.plt.rcParams[key]
