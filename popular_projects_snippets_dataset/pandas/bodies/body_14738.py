# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py

df = tm.makeTimeDataFrame()
ax = df.plot(x_compat=True)
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
self._check_ticks_props(ax, xrot=30)

tm.close()
plotting.plot_params["xaxis.compat"] = True
ax = df.plot()
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
self._check_ticks_props(ax, xrot=30)

tm.close()
plotting.plot_params["x_compat"] = False

ax = df.plot()
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)

tm.close()
# useful if you're plotting a bunch together
with plotting.plot_params.use("x_compat", True):
    ax = df.plot()
    lines = ax.get_lines()
    assert not isinstance(lines[0].get_xdata(), PeriodIndex)
    self._check_ticks_props(ax, xrot=30)

tm.close()
ax = df.plot()
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)
self._check_ticks_props(ax, xrot=0)
