# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
yrs = [3.5, 11]

xpl1 = xpl2 = [Period("1988Q1").ordinal] * len(yrs)
rs1 = []
rs2 = []
for n in yrs:
    rng = period_range("1987Q2", periods=int(n * 4), freq="Q")
    ser = Series(np.random.randn(len(rng)), rng)
    _, ax = self.plt.subplots()
    ser.plot(ax=ax)
    xaxis = ax.get_xaxis()
    rs1.append(xaxis.get_majorticklocs()[0])

    (vmin, vmax) = ax.get_xlim()
    ax.set_xlim(vmin + 0.9, vmax)
    rs2.append(xaxis.get_majorticklocs()[0])
    self.plt.close(ax.get_figure())

assert rs1 == xpl1
assert rs2 == xpl2
