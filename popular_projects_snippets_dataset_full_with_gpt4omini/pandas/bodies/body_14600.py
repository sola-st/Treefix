# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
xp = [1987, 1988, 1990, 1990, 1995, 2020, 2070, 2170]
xp = [Period(x, freq="A").ordinal for x in xp]
rs = []
for nyears in [5, 10, 19, 49, 99, 199, 599, 1001]:
    rng = period_range("1987", periods=nyears, freq="A")
    ser = Series(np.random.randn(len(rng)), rng)
    _, ax = self.plt.subplots()
    ser.plot(ax=ax)
    xaxis = ax.get_xaxis()
    rs.append(xaxis.get_majorticklocs()[0])
    self.plt.close(ax.get_figure())

assert rs == xp
