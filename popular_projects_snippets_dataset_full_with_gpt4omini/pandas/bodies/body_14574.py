# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
def check_format_of_first_point(ax, expected_string):
    first_line = ax.get_lines()[0]
    first_x = first_line.get_xdata()[0].ordinal
    first_y = first_line.get_ydata()[0]
    assert expected_string == ax.format_coord(first_x, first_y)

annual = Series(1, index=date_range("2014-01-01", periods=3, freq="A-DEC"))
_, ax = self.plt.subplots()
annual.plot(ax=ax)
check_format_of_first_point(ax, "t = 2014  y = 1.000000")

# note this is added to the annual plot already in existence, and
# changes its freq field
daily = Series(1, index=date_range("2014-01-01", periods=3, freq="D"))
daily.plot(ax=ax)
check_format_of_first_point(ax, "t = 2014-01-01  y = 1.000000")
tm.close()
