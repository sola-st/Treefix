# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
values = [1, 2, np.nan, 3]
d = Series(values, index=index)
ax = _check_plot_works(d.plot)
masked = ax.lines[0].get_ydata()
# remove nan for comparison purpose
exp = np.array([1, 2, 3], dtype=np.float64)
tm.assert_numpy_array_equal(np.delete(masked.data, 2), exp)
tm.assert_numpy_array_equal(masked.mask, np.array([False, False, True, False]))

expected = np.array([1, 2, 0, 3], dtype=np.float64)
ax = _check_plot_works(d.plot, stacked=True)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
ax = _check_plot_works(d.plot.area)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
ax = _check_plot_works(d.plot.area, stacked=False)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
