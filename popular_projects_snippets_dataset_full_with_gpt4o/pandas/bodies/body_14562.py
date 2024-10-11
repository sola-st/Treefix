# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH2877, GH17173, GH31205, GH31580
tz = tz_aware_fixture
index = date_range("1/1/2011", periods=2, freq="H", tz=tz)
ts = Series([188.5, 328.25], index=index)
_check_plot_works(ts.plot)
ax = ts.plot()
xdata = list(ax.get_lines())[0].get_xdata()
# Check first and last points' labels are correct
assert (xdata[0].hour, xdata[0].minute) == (0, 0)
assert (xdata[-1].hour, xdata[-1].minute) == (1, 0)
