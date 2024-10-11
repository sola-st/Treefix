# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idxh = date_range("1/1/1999", periods=52, freq="W")
idxl = date_range("1/1/1999", periods=12, freq="M")
high = DataFrame(np.random.rand(len(idxh), 3), index=idxh, columns=[0, 1, 2])
low = DataFrame(np.random.rand(len(idxl), 3), index=idxl, columns=[0, 1, 2])

# low to high
for kind1, kind2 in [("line", "area"), ("area", "line")]:
    _, ax = self.plt.subplots()
    low.plot(kind=kind1, stacked=True, ax=ax)
    high.plot(kind=kind2, stacked=True, ax=ax)

    # check low dataframe result
    expected_x = np.array(
        [
            1514,
            1519,
            1523,
            1527,
            1531,
            1536,
            1540,
            1544,
            1549,
            1553,
            1558,
            1562,
        ],
        dtype=np.float64,
    )
    expected_y = np.zeros(len(expected_x), dtype=np.float64)
    for i in range(3):
        line = ax.lines[i]
        assert PeriodIndex(line.get_xdata()).freq == idxh.freq
        tm.assert_numpy_array_equal(line.get_xdata(orig=False), expected_x)
        # check stacked values are correct
        expected_y += low[i].values
        tm.assert_numpy_array_equal(line.get_ydata(orig=False), expected_y)

    # check high dataframe result
    expected_x = idxh.to_period().asi8.astype(np.float64)
    expected_y = np.zeros(len(expected_x), dtype=np.float64)
    for i in range(3):
        line = ax.lines[3 + i]
        assert PeriodIndex(data=line.get_xdata()).freq == idxh.freq
        tm.assert_numpy_array_equal(line.get_xdata(orig=False), expected_x)
        expected_y += high[i].values
        tm.assert_numpy_array_equal(line.get_ydata(orig=False), expected_y)

        # high to low
for kind1, kind2 in [("line", "area"), ("area", "line")]:
    _, ax = self.plt.subplots()
    high.plot(kind=kind1, stacked=True, ax=ax)
    low.plot(kind=kind2, stacked=True, ax=ax)

    # check high dataframe result
    expected_x = idxh.to_period().asi8.astype(np.float64)
    expected_y = np.zeros(len(expected_x), dtype=np.float64)
    for i in range(3):
        line = ax.lines[i]
        assert PeriodIndex(data=line.get_xdata()).freq == idxh.freq
        tm.assert_numpy_array_equal(line.get_xdata(orig=False), expected_x)
        expected_y += high[i].values
        tm.assert_numpy_array_equal(line.get_ydata(orig=False), expected_y)

    # check low dataframe result
    expected_x = np.array(
        [
            1514,
            1519,
            1523,
            1527,
            1531,
            1536,
            1540,
            1544,
            1549,
            1553,
            1558,
            1562,
        ],
        dtype=np.float64,
    )
    expected_y = np.zeros(len(expected_x), dtype=np.float64)
    for i in range(3):
        lines = ax.lines[3 + i]
        assert PeriodIndex(data=lines.get_xdata()).freq == idxh.freq
        tm.assert_numpy_array_equal(lines.get_xdata(orig=False), expected_x)
        expected_y += low[i].values
        tm.assert_numpy_array_equal(lines.get_ydata(orig=False), expected_y)
