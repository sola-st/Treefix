# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 10962
df = DataFrame(np.random.rand(5, 5), columns=list("aaaaa"))
axes = df.plot(subplots=True)
for ax in axes:
    self._check_legend_labels(ax, labels=["a"])
    assert len(ax.lines) == 1
tm.close()

axes = df.plot(subplots=True, secondary_y="a")
for ax in axes:
    # (right) is only attached when subplots=False
    self._check_legend_labels(ax, labels=["a"])
    assert len(ax.lines) == 1
tm.close()

ax = df.plot(secondary_y="a")
self._check_legend_labels(ax, labels=["a (right)"] * 5)
assert len(ax.lines) == 0
assert len(ax.right_ax.lines) == 5
