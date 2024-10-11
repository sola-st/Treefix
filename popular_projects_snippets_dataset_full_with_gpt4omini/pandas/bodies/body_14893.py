# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 9779
df = DataFrame(np.random.randn(30, 3), columns=list("abc"))
s = Series(np.random.randn(30), name="x")

# primary -> secondary (without passing ax)
_, ax = self.plt.subplots()
ax = df.plot(ax=ax)
s.plot(legend=True, secondary_y=True, ax=ax)
# both legends are drawn on left ax
# left and right axis must be visible
self._check_legend_labels(ax, labels=["a", "b", "c", "x (right)"])
assert ax.get_yaxis().get_visible()
assert ax.right_ax.get_yaxis().get_visible()
tm.close()

# primary -> secondary (with passing ax)
_, ax = self.plt.subplots()
ax = df.plot(ax=ax)
s.plot(ax=ax, legend=True, secondary_y=True)
# both legends are drawn on left ax
# left and right axis must be visible
self._check_legend_labels(ax, labels=["a", "b", "c", "x (right)"])
assert ax.get_yaxis().get_visible()
assert ax.right_ax.get_yaxis().get_visible()
tm.close()

# secondary -> secondary (without passing ax)
_, ax = self.plt.subplots()
ax = df.plot(secondary_y=True, ax=ax)
s.plot(legend=True, secondary_y=True, ax=ax)
# both legends are drawn on left ax
# left axis must be invisible and right axis must be visible
expected = ["a (right)", "b (right)", "c (right)", "x (right)"]
self._check_legend_labels(ax.left_ax, labels=expected)
assert not ax.left_ax.get_yaxis().get_visible()
assert ax.get_yaxis().get_visible()
tm.close()

# secondary -> secondary (with passing ax)
_, ax = self.plt.subplots()
ax = df.plot(secondary_y=True, ax=ax)
s.plot(ax=ax, legend=True, secondary_y=True)
# both legends are drawn on left ax
# left axis must be invisible and right axis must be visible
expected = ["a (right)", "b (right)", "c (right)", "x (right)"]
self._check_legend_labels(ax.left_ax, expected)
assert not ax.left_ax.get_yaxis().get_visible()
assert ax.get_yaxis().get_visible()
tm.close()

# secondary -> secondary (with passing ax)
_, ax = self.plt.subplots()
ax = df.plot(secondary_y=True, mark_right=False, ax=ax)
s.plot(ax=ax, legend=True, secondary_y=True)
# both legends are drawn on left ax
# left axis must be invisible and right axis must be visible
expected = ["a", "b", "c", "x (right)"]
self._check_legend_labels(ax.left_ax, expected)
assert not ax.left_ax.get_yaxis().get_visible()
assert ax.get_yaxis().get_visible()
tm.close()
