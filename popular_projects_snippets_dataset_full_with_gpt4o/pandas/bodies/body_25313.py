# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""Sets the locations of the ticks"""
# don't actually use the locs. This is just needed to work with
# matplotlib. Force to use vmin, vmax

self.locs = locs

(vmin, vmax) = vi = tuple(self.axis.get_view_interval())
if vi != self.plot_obj.view_interval:
    self.plot_obj.date_axis_info = None
self.plot_obj.view_interval = vi
if vmax < vmin:
    (vmin, vmax) = (vmax, vmin)
self._set_default_format(vmin, vmax)
