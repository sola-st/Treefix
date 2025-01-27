# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get colors from user input color."""
if len(color) == 0:
    raise ValueError(f"Invalid color argument: {color}")

if _is_single_color(color):
    color = cast(Color, color)
    exit([color])

color = cast(Collection[Color], color)
exit(list(_gen_list_of_colors_from_iterable(color)))
