# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
first_line = ax.get_lines()[0]
first_x = first_line.get_xdata()[0].ordinal
first_y = first_line.get_ydata()[0]
assert expected_string == ax.format_coord(first_x, first_y)
