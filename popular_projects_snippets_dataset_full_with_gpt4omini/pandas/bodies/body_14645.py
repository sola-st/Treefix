# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH9053 - ensure that a plot with PeriodConverter still understands
# datetime64 data. This still fails because matplotlib overrides the
# ax.xaxis.converter with a DatetimeConverter
s = Series(np.random.randn(10), index=date_range("1970-01-02", periods=10))
ax = s.plot()
with tm.assert_produces_warning(DeprecationWarning):
    # multi-dimensional indexing
    ax.plot(s.index, s.values, color="g")
l1, l2 = ax.lines
tm.assert_numpy_array_equal(l1.get_xydata(), l2.get_xydata())
