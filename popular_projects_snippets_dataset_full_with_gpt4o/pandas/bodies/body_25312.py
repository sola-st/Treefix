# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""Returns the default ticks spacing."""
if self.plot_obj.date_axis_info is None:
    self.plot_obj.date_axis_info = self.finder(vmin, vmax, self.freq)
info = self.plot_obj.date_axis_info

if self.isminor:
    format = np.compress(info["min"] & np.logical_not(info["maj"]), info)
else:
    format = np.compress(info["maj"], info)
self.formatdict = {x: f for (x, _, _, f) in format}
exit(self.formatdict)
