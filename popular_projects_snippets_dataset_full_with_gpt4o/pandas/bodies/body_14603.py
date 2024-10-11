# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
ts = tm.makeTimeSeries()
ts.iloc[5:25] = np.nan
_, ax = self.plt.subplots()
ts.plot(ax=ax)
lines = ax.get_lines()
assert len(lines) == 1
line = lines[0]
data = line.get_xydata()

data = np.ma.MaskedArray(data, mask=isna(data), fill_value=np.nan)

assert isinstance(data, np.ma.core.MaskedArray)
mask = data.mask
assert mask[5:25, 1].all()
self.plt.close(ax.get_figure())

# irregular
ts = tm.makeTimeSeries()
ts = ts[[0, 1, 2, 5, 7, 9, 12, 15, 20]]
ts.iloc[2:5] = np.nan
_, ax = self.plt.subplots()
ax = ts.plot(ax=ax)
lines = ax.get_lines()
assert len(lines) == 1
line = lines[0]
data = line.get_xydata()

data = np.ma.MaskedArray(data, mask=isna(data), fill_value=np.nan)

assert isinstance(data, np.ma.core.MaskedArray)
mask = data.mask
assert mask[2:5, 1].all()
self.plt.close(ax.get_figure())

# non-ts
idx = [0, 1, 2, 5, 7, 9, 12, 15, 20]
ser = Series(np.random.randn(len(idx)), idx)
ser.iloc[2:5] = np.nan
_, ax = self.plt.subplots()
ser.plot(ax=ax)
lines = ax.get_lines()
assert len(lines) == 1
line = lines[0]
data = line.get_xydata()
data = np.ma.MaskedArray(data, mask=isna(data), fill_value=np.nan)

assert isinstance(data, np.ma.core.MaskedArray)
mask = data.mask
assert mask[2:5, 1].all()
