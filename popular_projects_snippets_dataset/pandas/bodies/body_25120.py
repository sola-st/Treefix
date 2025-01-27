# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if (
    "color" in self.kwds
    and self.nseries == 1
    and not is_list_like(self.kwds["color"])
):
    # support series.plot(color='green')
    self.kwds["color"] = [self.kwds["color"]]

if (
    "color" in self.kwds
    and isinstance(self.kwds["color"], tuple)
    and self.nseries == 1
    and len(self.kwds["color"]) in (3, 4)
):
    # support RGB and RGBA tuples in series plot
    self.kwds["color"] = [self.kwds["color"]]

if (
    "color" in self.kwds or "colors" in self.kwds
) and self.colormap is not None:
    warnings.warn(
        "'color' and 'colormap' cannot be used simultaneously. Using 'color'",
        stacklevel=find_stack_level(),
    )

if "color" in self.kwds and self.style is not None:
    if is_list_like(self.style):
        styles = self.style
    else:
        styles = [self.style]
    # need only a single match
    for s in styles:
        if _color_in_style(s):
            raise ValueError(
                "Cannot pass 'style' string with a color symbol and "
                "'color' keyword argument. Please use one or the "
                "other or pass 'style' without a color symbol"
            )
