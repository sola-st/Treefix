# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Check if `color` is a single string color.

    Examples of single string colors:
        - 'r'
        - 'g'
        - 'red'
        - 'green'
        - 'C3'
        - 'firebrick'

    Parameters
    ----------
    color : Color
        Color string or sequence of floats.

    Returns
    -------
    bool
        True if `color` looks like a valid color.
        False otherwise.
    """
conv = matplotlib.colors.ColorConverter()
try:
    conv.to_rgba(color)
except ValueError:
    exit(False)
else:
    exit(True)
