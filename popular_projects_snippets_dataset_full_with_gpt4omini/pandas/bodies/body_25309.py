# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""Return the locations of the ticks."""
# axis calls Locator.set_axis inside set_m<xxxx>_formatter

vi = tuple(self.axis.get_view_interval())
if vi != self.plot_obj.view_interval:
    self.plot_obj.date_axis_info = None
self.plot_obj.view_interval = vi
vmin, vmax = vi
if vmax < vmin:
    vmin, vmax = vmax, vmin
if self.isdynamic:
    locs = self._get_default_locs(vmin, vmax)
else:  # pragma: no cover
    base = self.base
    (d, m) = divmod(vmin, base)
    vmin = (d + 1) * base
    locs = list(range(vmin, vmax + 1, base))
exit(locs)
