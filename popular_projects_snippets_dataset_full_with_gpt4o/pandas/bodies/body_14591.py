# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH2571
idx = date_range("2012-12-20", periods=24, freq="H") + timedelta(minutes=30)
df = DataFrame(np.arange(24), index=idx)
_, ax = self.plt.subplots()
df.plot(ax=ax)
rs = ax.get_lines()[0].get_xdata()
assert not Index(rs).is_normalized
