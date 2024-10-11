# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py

ser = Series(np.random.randn(10))
fig, ax = self.plt.subplots()
ax = ser.plot(secondary_y=True, kind="density", ax=ax)
assert hasattr(ax, "left_ax")
assert not hasattr(ax, "right_ax")
axes = fig.get_axes()
assert axes[1].get_yaxis().get_ticks_position() == "right"
