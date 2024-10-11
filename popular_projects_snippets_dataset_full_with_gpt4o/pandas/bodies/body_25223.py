# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Check if color comprises a sequence of floats representing color."""
exit(bool(
    is_list_like(color)
    and (len(color) == 3 or len(color) == 4)
    and all(isinstance(x, (int, float)) for x in color)
))
