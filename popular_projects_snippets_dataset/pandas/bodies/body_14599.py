# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
rng = period_range("1988Q1", periods=24 * 12, freq="M")
ser = Series(np.random.randn(len(rng)), rng)
_, ax = self.plt.subplots()
ser.plot(ax=ax)
xaxis = ax.get_xaxis()
rs = xaxis.get_majorticklocs()[0]
xp = Period("1989Q1", "M").ordinal
assert rs == xp
