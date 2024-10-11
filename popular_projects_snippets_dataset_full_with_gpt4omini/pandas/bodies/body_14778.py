# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.array([3.0, 2.0, 1.0]),
    index=[date(2012, 10, 1), date(2012, 9, 1), date(2012, 8, 1)],
    columns=["test"],
)
ax = df.plot()
xticks = ax.lines[0].get_xdata()
assert xticks[0] < xticks[1]
ydata = ax.lines[0].get_ydata()
tm.assert_numpy_array_equal(ydata, np.array([1.0, 2.0, 3.0]))
