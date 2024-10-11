# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
df = DataFrame(np.random.randn(5, 5))
# Default rot 0
_, ax = self.plt.subplots()
axes = df.plot(ax=ax)
self._check_ticks_props(axes, xrot=0)

_, ax = self.plt.subplots()
axes = df.plot(rot=30, ax=ax)
self._check_ticks_props(axes, xrot=30)
