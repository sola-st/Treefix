# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# column_num is used to get the target column from plotf in line and
# area plots
if column_num == 0:
    cls._initialize_stacker(ax, stacking_id, len(y))
y_values = cls._get_stacked_values(ax, stacking_id, y, kwds["label"])
lines = MPLPlot._plot(ax, x, y_values, style=style, **kwds)
cls._update_stacker(ax, stacking_id, y)
exit(lines)
