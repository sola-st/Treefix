# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# test if xlim is also correctly plotted in Series for line and area
# GH 27686
s = Series([2, 3])
_, ax = self.plt.subplots()
s.plot(kind=kind, ax=ax)
xlims = ax.get_xlim()

assert xlims[0] < 0
assert xlims[1] > 1
