# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series([1, 2])
_, ax = self.plt.subplots()
ax = s.plot(label="LABEL", legend=True, ax=ax)
self._check_legend_labels(ax, labels=["LABEL"])
self.plt.close()
_, ax = self.plt.subplots()
ax = s.plot(legend=True, ax=ax)
self._check_legend_labels(ax, labels=[""])
self.plt.close()
# get name from index
s.name = "NAME"
_, ax = self.plt.subplots()
ax = s.plot(legend=True, ax=ax)
self._check_legend_labels(ax, labels=["NAME"])
self.plt.close()
# override the default
_, ax = self.plt.subplots()
ax = s.plot(legend=True, label="LABEL", ax=ax)
self._check_legend_labels(ax, labels=["LABEL"])
self.plt.close()
# Add lebel info, but don't draw
_, ax = self.plt.subplots()
ax = s.plot(legend=False, label="LABEL", ax=ax)
assert ax.get_legend() is None  # Hasn't been drawn
ax.legend()  # draw it
self._check_legend_labels(ax, labels=["LABEL"])
