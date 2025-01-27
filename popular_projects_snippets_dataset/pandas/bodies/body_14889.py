# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from pandas.plotting._matplotlib.converter import DatetimeConverter

rng = date_range("1/1/2000", "3/1/2000")
rng = rng[[0, 1, 2, 3, 5, 9, 10, 11, 12]]
ser = Series(np.random.randn(len(rng)), rng)
_, ax = self.plt.subplots()
ax = ser.plot(ax=ax)
xp = DatetimeConverter.convert(datetime(1999, 1, 1), "", ax)
ax.set_xlim("1/1/1999", "1/1/2001")
assert xp == ax.get_xlim()[0]
self._check_ticks_props(ax, xrot=30)
