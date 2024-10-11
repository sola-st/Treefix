# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
ser = Series(
    [0.0, 1.0, np.nan, 3.0, 4.0, 5.0, 6.0],
    index=[1.0, 0.0, 3.0, 2.0, np.nan, 3.0, 2.0],
)
_, ax = self.plt.subplots()
ax = ser.plot(ax=ax)
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= np.nanmin(lines[0].get_data(orig=False)[0])
assert xmax >= np.nanmax(lines[0].get_data(orig=False)[0])
