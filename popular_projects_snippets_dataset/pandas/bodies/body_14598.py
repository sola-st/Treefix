# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
yrs = [1.15, 2.5, 4, 11]

xpl1 = xpl2 = [Period("Jan 1988").ordinal] * len(yrs)
rs1 = []
rs2 = []
for n in yrs:
    rng = period_range("1987Q2", periods=int(n * 12), freq="M")
    ser = Series(np.random.randn(len(rng)), rng)
    _, ax = self.plt.subplots()
    ser.plot(ax=ax)
    xaxis = ax.get_xaxis()
    rs1.append(xaxis.get_majorticklocs()[0])

    vmin, vmax = ax.get_xlim()
    ax.set_xlim(vmin + 0.9, vmax)
    rs2.append(xaxis.get_majorticklocs()[0])
    self.plt.close(ax.get_figure())

assert rs1 == xpl1
assert rs2 == xpl2
