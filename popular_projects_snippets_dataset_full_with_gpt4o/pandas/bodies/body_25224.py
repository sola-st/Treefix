# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get colors from user input color type."""
if color_type == "default":
    exit(_get_default_colors(num_colors))
elif color_type == "random":
    exit(_get_random_colors(num_colors))
else:
    raise ValueError("color_type must be either 'default' or 'random'")
