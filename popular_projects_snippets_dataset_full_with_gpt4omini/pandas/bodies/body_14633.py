# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
dates = [date(2008, 12, 31), date(2009, 1, 31)]
values1 = np.arange(10.0, 11.0, 0.5)
values2 = np.arange(11.0, 12.0, 0.5)

kw = {"fmt": "-", "lw": 4}

_, ax = self.plt.subplots()
ax.plot_date([x.toordinal() for x in dates], values1, **kw)
ax.plot_date([x.toordinal() for x in dates], values2, **kw)

line1, line2 = ax.get_lines()

exp = np.array([x.toordinal() for x in dates], dtype=np.float64)
tm.assert_numpy_array_equal(line1.get_xydata()[:, 0], exp)
exp = np.array([x.toordinal() for x in dates], dtype=np.float64)
tm.assert_numpy_array_equal(line2.get_xydata()[:, 0], exp)
