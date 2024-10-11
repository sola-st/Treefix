# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if num_colors is None:
    num_colors = self.nseries

exit(get_standard_colors(
    num_colors=num_colors,
    colormap=self.colormap,
    color=self.kwds.get(color_kwds),
))
