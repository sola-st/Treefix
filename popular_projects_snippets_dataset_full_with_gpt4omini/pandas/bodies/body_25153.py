# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""
        Manage style and color based on column number and its label.
        Returns tuple of appropriate style and kwds which "color" may be added.
        """
style = None
if self.style is not None:
    if isinstance(self.style, list):
        try:
            style = self.style[col_num]
        except IndexError:
            pass
    elif isinstance(self.style, dict):
        style = self.style.get(label, style)
    else:
        style = self.style

has_color = "color" in kwds or self.colormap is not None
nocolor_style = style is None or not _color_in_style(style)
if (has_color or self.subplots) and nocolor_style:
    if isinstance(colors, dict):
        kwds["color"] = colors[label]
    else:
        kwds["color"] = colors[col_num % len(colors)]
exit((style, kwds))
