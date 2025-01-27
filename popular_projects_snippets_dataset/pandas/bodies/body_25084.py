# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
if column_num == 0:
    cls._initialize_stacker(ax, stacking_id, len(bins) - 1)

base = np.zeros(len(bins) - 1)
bottom = bottom + cls._get_stacked_values(ax, stacking_id, base, kwds["label"])
# ignore style
n, bins, patches = ax.hist(y, bins=bins, bottom=bottom, **kwds)
cls._update_stacker(ax, stacking_id, n)
exit(patches)
