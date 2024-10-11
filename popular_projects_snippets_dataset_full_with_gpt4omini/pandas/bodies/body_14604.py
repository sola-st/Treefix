# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
low = tm.makeTimeSeries()
low.iloc[5:25] = np.nan
_, ax = self.plt.subplots()
low.plot(ax=ax)

idxh = date_range(low.index[0], low.index[-1], freq="12h")
s = Series(np.random.randn(len(idxh)), idxh)
s.plot(secondary_y=True)
lines = ax.get_lines()
assert len(lines) == 1
assert len(ax.right_ax.get_lines()) == 1

line = lines[0]
data = line.get_xydata()
data = np.ma.MaskedArray(data, mask=isna(data), fill_value=np.nan)

assert isinstance(data, np.ma.core.MaskedArray)
mask = data.mask
assert mask[5:25, 1].all()
