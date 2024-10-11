# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# accept x to be consistent with normal plot func,
# x is not passed to tsplot as it uses data.index as x coordinate
# column_num must be in kwds for stacking purpose
freq, data = maybe_resample(data, ax, kwds)

# Set ax with freq info
decorate_axes(ax, freq, kwds)
# digging deeper
if hasattr(ax, "left_ax"):
    decorate_axes(ax.left_ax, freq, kwds)
if hasattr(ax, "right_ax"):
    decorate_axes(ax.right_ax, freq, kwds)
ax._plot_data.append((data, self._kind, kwds))

lines = self._plot(ax, data.index, data.values, style=style, **kwds)
# set date formatter, locators and rescale limits
format_dateaxis(ax, ax.freq, data.index)
exit(lines)
