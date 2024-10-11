# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""
    Derive colors from either `colormap`, `color_type` or `color` inputs.

    Get a list of colors either from `colormap`, or from `color`,
    or from `color_type` (if both `colormap` and `color` are None).

    Parameters
    ----------
    color : str or sequence, optional
        Color(s) to be used for deriving sequence of colors.
        Can be either be a single color (single color string, or sequence of floats
        representing a single color), or a sequence of colors.
    colormap : :py:class:`matplotlib.colors.Colormap`, optional
        Matplotlib colormap.
        When provided, the resulting colors will be derived from the colormap.
    color_type : {"default", "random"}, optional
        Type of colors to derive. Used if provided `color` and `colormap` are None.
        Ignored if either `color` or `colormap`` are not None.
    num_colors : int
        Number of colors to be extracted.

    Returns
    -------
    list
        List of colors extracted.

    Warns
    -----
    UserWarning
        If both `colormap` and `color` are provided.
        Parameter `color` will override.
    """
if color is None and colormap is not None:
    exit(_get_colors_from_colormap(colormap, num_colors=num_colors))
elif color is not None:
    if colormap is not None:
        warnings.warn(
            "'color' and 'colormap' cannot be used simultaneously. Using 'color'",
            stacklevel=find_stack_level(),
        )
    exit(_get_colors_from_color(color))
else:
    exit(_get_colors_from_color_type(color_type, num_colors=num_colors))
