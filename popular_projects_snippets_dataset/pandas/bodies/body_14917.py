# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
ser = Series([1, 2, 3, 4])
_, ax = self.plt.subplots()
ax = ser.plot(ax=ax)
before = ax.xaxis.get_ticklocs()

ser.drop([0, 1], inplace=True)
_, ax = self.plt.subplots()
after = ax.xaxis.get_ticklocs()
tm.assert_numpy_array_equal(before, after)
