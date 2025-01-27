# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 9610
df = DataFrame(np.random.randn(30, 4), columns=list("abcd"))

# primary -> secondary
_, ax = self.plt.subplots()
ax = df["a"].plot.hist(legend=True, ax=ax)
df["b"].plot.hist(ax=ax, legend=True, secondary_y=True)
# both legends are drawn on left ax
# left and right axis must be visible
self._check_legend_labels(ax, labels=["a", "b (right)"])
assert ax.get_yaxis().get_visible()
assert ax.right_ax.get_yaxis().get_visible()
tm.close()

# secondary -> secondary
_, ax = self.plt.subplots()
ax = df["a"].plot.hist(legend=True, secondary_y=True, ax=ax)
df["b"].plot.hist(ax=ax, legend=True, secondary_y=True)
# both legends are draw on left ax
# left axis must be invisible, right axis must be visible
self._check_legend_labels(ax.left_ax, labels=["a (right)", "b (right)"])
assert not ax.left_ax.get_yaxis().get_visible()
assert ax.get_yaxis().get_visible()
tm.close()

# secondary -> primary
_, ax = self.plt.subplots()
ax = df["a"].plot.hist(legend=True, secondary_y=True, ax=ax)
# right axes is returned
df["b"].plot.hist(ax=ax, legend=True)
# both legends are draw on left ax
# left and right axis must be visible
self._check_legend_labels(ax.left_ax, labels=["a (right)", "b"])
assert ax.left_ax.get_yaxis().get_visible()
assert ax.get_yaxis().get_visible()
tm.close()
