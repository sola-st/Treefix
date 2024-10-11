# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 3490 - mixed frequency timeseries with secondary y
rng = date_range("2000-01-01", periods=10000, freq="min")
ts = Series(1, index=rng)

_, ax = self.plt.subplots()
ts.plot(ax=ax)
left_before, right_before = ax.get_xlim()
ts.resample("D").mean().plot(secondary_y=True, ax=ax)
left_after, right_after = ax.get_xlim()

# a downsample should not have changed either limit
assert left_before == left_after
assert right_before == right_after
