# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# get the twinx ax if appropriate
if self.subplots:
    i = self._col_idx_to_axis_idx(i)
    ax = self.axes[i]
    ax = self._maybe_right_yaxis(ax, i)
    self.axes[i] = ax
else:
    ax = self.axes[0]
    ax = self._maybe_right_yaxis(ax, i)

ax.get_yaxis().set_visible(True)
exit(ax)
