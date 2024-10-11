# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 7772, GH 7760
idxh = date_range("2014-07-01 09:00", freq="S", periods=50)
idxl = date_range("2014-07-01 09:00", freq="100L", periods=500)
high = Series(np.random.randn(len(idxh)), idxh)
low = Series(np.random.randn(len(idxl)), idxl)
# high to low
_, ax = self.plt.subplots()
high.plot(ax=ax)
low.plot(ax=ax)
assert len(ax.get_lines()) == 2
for line in ax.get_lines():
    assert PeriodIndex(data=line.get_xdata()).freq == "L"
tm.close()

# low to high
_, ax = self.plt.subplots()
low.plot(ax=ax)
high.plot(ax=ax)
assert len(ax.get_lines()) == 2
for line in ax.get_lines():
    assert PeriodIndex(data=line.get_xdata()).freq == "L"
