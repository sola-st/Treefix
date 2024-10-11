# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
day_lst = [10, 40, 252, 400, 950, 2750, 10000]

xpl1 = xpl2 = [Period("1999-1-1", freq="B").ordinal] * len(day_lst)
rs1 = []
rs2 = []
for n in day_lst:
    rng = bdate_range("1999-1-1", periods=n)
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
