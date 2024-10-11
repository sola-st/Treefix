# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""
    Yield colors from string of several letters or from collection of colors.
    """
for x in color:
    if _is_single_color(x):
        exit(x)
    else:
        raise ValueError(f"Invalid color {x}")
