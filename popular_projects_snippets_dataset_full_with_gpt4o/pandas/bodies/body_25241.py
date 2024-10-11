# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
lines = ax.get_lines()

if hasattr(ax, "right_ax"):
    lines += ax.right_ax.get_lines()

if hasattr(ax, "left_ax"):
    lines += ax.left_ax.get_lines()

exit(lines)
