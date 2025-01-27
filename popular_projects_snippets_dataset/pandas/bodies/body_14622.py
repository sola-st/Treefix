# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idxh = date_range("1/1/1999", periods=52, freq="W")
idxl = date_range("1/1/1999", periods=12, freq="M")
high = Series(np.random.randn(len(idxh)), idxh)
low = Series(np.random.randn(len(idxl)), idxl)
_, ax = self.plt.subplots()
low.plot(ax=ax)
high.plot(ax=ax)

expected_h = idxh.to_period().asi8.astype(np.float64)
expected_l = np.array(
    [1514, 1519, 1523, 1527, 1531, 1536, 1540, 1544, 1549, 1553, 1558, 1562],
    dtype=np.float64,
)
for line in ax.get_lines():
    assert PeriodIndex(data=line.get_xdata()).freq == idxh.freq
    xdata = line.get_xdata(orig=False)
    if len(xdata) == 12:  # idxl lines
        tm.assert_numpy_array_equal(xdata, expected_l)
    else:
        tm.assert_numpy_array_equal(xdata, expected_h)
tm.close()
