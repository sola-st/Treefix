# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
_, ax = self.plt.subplots()
rng = date_range("2001-1-1", "2001-1-10")
ts = Series(range(len(rng)), index=rng)
ts = concat([ts[:3], ts[5:]])
ts.plot(ax=ax)
assert not hasattr(ax, "freq")
