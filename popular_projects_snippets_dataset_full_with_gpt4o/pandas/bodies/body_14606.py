# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = date_range("1/1/2000", periods=10)
ser = Series(np.random.randn(10), idx)
ser2 = Series(np.random.randn(10), idx)
fig, _ = self.plt.subplots()
ax = ser.plot(secondary_y=True)
assert hasattr(ax, "left_ax")
assert not hasattr(ax, "right_ax")
axes = fig.get_axes()
line = ax.get_lines()[0]
xp = Series(line.get_ydata(), line.get_xdata()).to_timestamp()
tm.assert_series_equal(ser, xp)
assert ax.get_yaxis().get_ticks_position() == "right"
assert not axes[0].get_yaxis().get_visible()
self.plt.close(fig)

_, ax2 = self.plt.subplots()
ser2.plot(ax=ax2)
assert ax2.get_yaxis().get_ticks_position() == "left"
self.plt.close(ax2.get_figure())

ax = ser2.plot()
ax2 = ser.plot(secondary_y=True)
assert ax.get_yaxis().get_visible()
