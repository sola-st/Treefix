# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idxh = date_range("1/1/1999", periods=365, freq="D")
idxl = date_range("1/1/1999", periods=12, freq="M")
high = Series(np.random.randn(len(idxh)), idxh)
low = Series(np.random.randn(len(idxl)), idxl)
_, ax = self.plt.subplots()
high.plot(ax=ax)
low.plot(ax=ax)
for line in ax.get_lines():
    assert PeriodIndex(data=line.get_xdata()).freq == "D"
