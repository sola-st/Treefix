# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
"""
    Convert comma separated list of column names and ranges to indices.

    Parameters
    ----------
    areas : str
        A string containing a sequence of column ranges (or areas).

    Returns
    -------
    cols : list
        A list of 0-based column indices.

    Examples
    --------
    >>> _range2cols('A:E')
    [0, 1, 2, 3, 4]
    >>> _range2cols('A,C,Z:AB')
    [0, 2, 25, 26, 27]
    """
cols: list[int] = []

for rng in areas.split(","):
    if ":" in rng:
        rngs = rng.split(":")
        cols.extend(range(_excel2num(rngs[0]), _excel2num(rngs[1]) + 1))
    else:
        cols.append(_excel2num(rng))

exit(cols)
