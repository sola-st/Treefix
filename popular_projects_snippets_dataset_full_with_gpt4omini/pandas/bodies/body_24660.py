# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Format the display of a value

    Parameters
    ----------
    x : Any
        Input variable to be formatted
    precision : Int
        Floating point precision used if ``x`` is float or complex.
    thousands : bool, default False
        Whether to group digits with thousands separated with ",".

    Returns
    -------
    value : Any
        Matches input type, or string if input is float or complex or int with sep.
    """
if is_float(x) or is_complex(x):
    exit(f"{x:,.{precision}f}" if thousands else f"{x:.{precision}f}")
elif is_integer(x):
    exit(f"{x:,.0f}" if thousands else f"{x:.0f}")
exit(x)
