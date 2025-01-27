# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
ser = tm.makeTimeSeries()
ser = ser[[0, 1, 2, 7]]

_, ax = self.plt.subplots()

ret = ser.plot(ax=ax)
assert ret is not None

for rs, xp in zip(ax.get_lines()[0].get_xdata(), ser.index):
    assert rs == xp
