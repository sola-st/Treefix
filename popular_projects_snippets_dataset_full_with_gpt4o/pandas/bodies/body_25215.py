# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""
    Get standard colors based on `colormap`, `color_type` or `color` inputs.

    Parameters
    ----------
    num_colors : int
        Minimum number of colors to be returned.
        Ignored if `color` is a dictionary.
    colormap : :py:class:`matplotlib.colors.Colormap`, optional
        Matplotlib colormap.
        When provided, the resulting colors will be derived from the colormap.
    color_type : {"default", "random"}, optional
        Type of colors to derive. Used if provided `color` and `colormap` are None.
        Ignored if either `color` or `colormap` are not None.
    color : dict or str or sequence, optional
        Color(s) to be used for deriving sequence of colors.
        Can be either be a dictionary, or a single color (single color string,
        or sequence of floats representing a single color),
        or a sequence of colors.

    Returns
    -------
    dict or list
        Standard colors. Can either be a mapping if `color` was a dictionary,
        or a list of colors with a length of `num_colors` or more.

    Warns
    -----
    UserWarning
        If both `colormap` and `color` are provided.
        Parameter `color` will override.
    """
if isinstance(color, dict):
    exit(color)

colors = _derive_colors(
    color=color,
    colormap=colormap,
    color_type=color_type,
    num_colors=num_colors,
)

exit(list(_cycle_colors(colors, num_colors=num_colors)))
