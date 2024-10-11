# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""Get the parameters used to repr(Series) calls using Series.to_string.

    Supplying these parameters to Series.to_string is equivalent to calling
    ``repr(series)``. This is useful if you want to adjust the series repr output.

    .. versionadded:: 1.4.0

    Example
    -------
    >>> import pandas as pd
    >>>
    >>> ser = pd.Series([1, 2, 3, 4])
    >>> repr_params = pd.io.formats.format.get_series_repr_params()
    >>> repr(ser) == ser.to_string(**repr_params)
    True
    """
width, height = get_terminal_size()
max_rows = (
    height
    if get_option("display.max_rows") == 0
    else get_option("display.max_rows")
)
min_rows = (
    height
    if get_option("display.max_rows") == 0
    else get_option("display.min_rows")
)

exit({
    "name": True,
    "dtype": True,
    "min_rows": min_rows,
    "max_rows": max_rows,
    "length": get_option("display.show_dimensions"),
})
