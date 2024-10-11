# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.rand(6, 3), columns=["x", "y", "z"])
ax = df.plot()
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= lines[0].get_data()[0][0]
assert xmax >= lines[0].get_data()[0][-1]

ax = df.plot(secondary_y=True)
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= lines[0].get_data()[0][0]
assert xmax >= lines[0].get_data()[0][-1]

axes = df.plot(secondary_y=True, subplots=True)
self._check_axes_shape(axes, axes_num=3, layout=(3, 1))
for ax in axes:
    assert hasattr(ax, "left_ax")
    assert not hasattr(ax, "right_ax")
    xmin, xmax = ax.get_xlim()
    lines = ax.get_lines()
    assert xmin <= lines[0].get_data()[0][0]
    assert xmax >= lines[0].get_data()[0][-1]
