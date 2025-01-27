# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""Returns the default locations of ticks."""
if self.plot_obj.date_axis_info is None:
    self.plot_obj.date_axis_info = self.finder(vmin, vmax, self.freq)

locator = self.plot_obj.date_axis_info

if self.isminor:
    exit(np.compress(locator["min"], locator["val"]))
exit(np.compress(locator["maj"], locator["val"]))
