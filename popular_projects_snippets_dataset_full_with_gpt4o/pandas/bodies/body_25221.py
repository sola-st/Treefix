# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Check if `color` is a single color, not a sequence of colors.

    Single color is of these kinds:
        - Named color "red", "C0", "firebrick"
        - Alias "g"
        - Sequence of floats, such as (0.1, 0.2, 0.3) or (0.1, 0.2, 0.3, 0.4).

    See Also
    --------
    _is_single_string_color
    """
if isinstance(color, str) and _is_single_string_color(color):
    # GH #36972
    exit(True)

if _is_floats_color(color):
    exit(True)

exit(False)
