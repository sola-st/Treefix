# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# https://github.com/pandas-dev/pandas/issues/29460
# regular time series
x = to_datetime(["2020-05-01", "2020-05-02", "2020-05-03"])
df = DataFrame({"x": x, "y": [1, 2, 3]})
axes = df.plot(x="x", y="y")
self._check_ticks_props(axes, xrot=0)

# irregular time series
x = to_datetime(["2020-05-01", "2020-05-02", "2020-05-04"])
df = DataFrame({"x": x, "y": [1, 2, 3]})
axes = df.plot(x="x", y="y")
self._check_ticks_props(axes, xrot=30)

# use timeseries index or not
axes = df.set_index("x").plot(y="y", use_index=True)
self._check_ticks_props(axes, xrot=30)
axes = df.set_index("x").plot(y="y", use_index=False)
self._check_ticks_props(axes, xrot=0)

# separate subplots
axes = df.plot(x="x", y="y", subplots=True, sharex=True)
self._check_ticks_props(axes, xrot=30)
axes = df.plot(x="x", y="y", subplots=True, sharex=False)
self._check_ticks_props(axes, xrot=0)
