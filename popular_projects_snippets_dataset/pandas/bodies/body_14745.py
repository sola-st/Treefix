# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
values1 = [1, 2, np.nan, 3]
values2 = [3, np.nan, 2, 1]
df = DataFrame({"a": values1, "b": values2})
tdf = DataFrame({"a": values1, "b": values2}, index=tm.makeDateIndex(k=4))

for d in [df, tdf]:
    ax = _check_plot_works(d.plot)
    masked1 = ax.lines[0].get_ydata()
    masked2 = ax.lines[1].get_ydata()
    # remove nan for comparison purpose

    exp = np.array([1, 2, 3], dtype=np.float64)
    tm.assert_numpy_array_equal(np.delete(masked1.data, 2), exp)

    exp = np.array([3, 2, 1], dtype=np.float64)
    tm.assert_numpy_array_equal(np.delete(masked2.data, 1), exp)
    tm.assert_numpy_array_equal(
        masked1.mask, np.array([False, False, True, False])
    )
    tm.assert_numpy_array_equal(
        masked2.mask, np.array([False, True, False, False])
    )

    expected1 = np.array([1, 2, 0, 3], dtype=np.float64)
    expected2 = np.array([3, 0, 2, 1], dtype=np.float64)

    ax = _check_plot_works(d.plot, stacked=True)
    tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
    tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected1 + expected2)

    ax = _check_plot_works(d.plot.area)
    tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
    tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected1 + expected2)

    ax = _check_plot_works(d.plot.area, stacked=False)
    tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
    tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected2)
