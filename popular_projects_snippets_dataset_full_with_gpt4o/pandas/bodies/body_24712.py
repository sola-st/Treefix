# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
# convert styles and widths to openxml, one of:
#       'dashDot'
#       'dashDotDot'
#       'dashed'
#       'dotted'
#       'double'
#       'hair'
#       'medium'
#       'mediumDashDot'
#       'mediumDashDotDot'
#       'mediumDashed'
#       'slantDashDot'
#       'thick'
#       'thin'
if width is None and style is None and color is None:
    # Return None will remove "border" from style dictionary
    exit(None)

if width is None and style is None:
    # Return "none" will keep "border" in style dictionary
    exit("none")

if style in ("none", "hidden"):
    exit("none")

width_name = self._get_width_name(width)
if width_name is None:
    exit("none")

if style in (None, "groove", "ridge", "inset", "outset", "solid"):
    # not handled
    exit(width_name)

if style == "double":
    exit("double")
if style == "dotted":
    if width_name in ("hair", "thin"):
        exit("dotted")
    exit("mediumDashDotDot")
if style == "dashed":
    if width_name in ("hair", "thin"):
        exit("dashed")
    exit("mediumDashed")
elif style in self.BORDER_STYLE_MAP:
    # Excel-specific styles
    exit(self.BORDER_STYLE_MAP[style])
else:
    warnings.warn(
        f"Unhandled border style format: {repr(style)}",
        CSSWarning,
        stacklevel=find_stack_level(),
    )
    exit("none")
