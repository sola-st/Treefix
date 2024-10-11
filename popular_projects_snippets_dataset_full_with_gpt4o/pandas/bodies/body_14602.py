# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
nhours = 23
rng = date_range("1/1/1999", freq="H", periods=nhours)
ser = Series(np.random.randn(len(rng)), rng)
_, ax = self.plt.subplots()
ser.plot(ax=ax)
xaxis = ax.get_xaxis()
rs = xaxis.get_majorticklocs()[0]
xp = Period("1/1/1999", freq="H").ordinal

assert rs == xp
