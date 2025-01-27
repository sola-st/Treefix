# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
def _test(ax):
    xlim = ax.get_xlim()
    ax.set_xlim(xlim[0] - 5, xlim[1] + 10)
    result = ax.get_xlim()
    assert result[0] == xlim[0] - 5
    assert result[1] == xlim[1] + 10

    # string
    expected = (Period("1/1/2000", ax.freq), Period("4/1/2000", ax.freq))
    ax.set_xlim("1/1/2000", "4/1/2000")
    result = ax.get_xlim()
    assert int(result[0]) == expected[0].ordinal
    assert int(result[1]) == expected[1].ordinal

    # datetime
    expected = (Period("1/1/2000", ax.freq), Period("4/1/2000", ax.freq))
    ax.set_xlim(datetime(2000, 1, 1), datetime(2000, 4, 1))
    result = ax.get_xlim()
    assert int(result[0]) == expected[0].ordinal
    assert int(result[1]) == expected[1].ordinal
    fig = ax.get_figure()
    self.plt.close(fig)

ser = tm.makeTimeSeries()
_, ax = self.plt.subplots()
ser.plot(ax=ax)
_test(ax)

_, ax = self.plt.subplots()
df = DataFrame({"a": ser, "b": ser + 1})
df.plot(ax=ax)
_test(ax)

df = DataFrame({"a": ser, "b": ser + 1})
axes = df.plot(subplots=True)

for ax in axes:
    _test(ax)
