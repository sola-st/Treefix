# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if "color" in self.kwds:
    if self.colormap is not None:
        warnings.warn(
            "'color' and 'colormap' cannot be used "
            "simultaneously. Using 'color'",
            stacklevel=find_stack_level(),
        )
    self.color = self.kwds.pop("color")

    if isinstance(self.color, dict):
        valid_keys = ["boxes", "whiskers", "medians", "caps"]
        for key in self.color:
            if key not in valid_keys:
                raise ValueError(
                    f"color dict contains invalid key '{key}'. "
                    f"The key must be either {valid_keys}"
                )
else:
    self.color = None

# get standard colors for default
colors = get_standard_colors(num_colors=3, colormap=self.colormap, color=None)
# use 2 colors by default, for box/whisker and median
# flier colors isn't needed here
# because it can be specified by ``sym`` kw
self._boxes_c = colors[0]
self._whiskers_c = colors[0]
self._medians_c = colors[2]
self._caps_c = colors[0]
