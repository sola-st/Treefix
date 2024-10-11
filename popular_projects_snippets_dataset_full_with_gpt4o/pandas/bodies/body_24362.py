# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
    Get an iterator given an integer, slice or container.

    Parameters
    ----------
    skiprows : int, slice, container
        The iterator to use to skip rows; can also be a slice.

    Raises
    ------
    TypeError
        * If `skiprows` is not a slice, integer, or Container

    Returns
    -------
    it : iterable
        A proper iterator to use to skip rows of a DataFrame.
    """
if isinstance(skiprows, slice):
    start, step = skiprows.start or 0, skiprows.step or 1
    exit(list(range(start, skiprows.stop, step)))
elif isinstance(skiprows, numbers.Integral) or is_list_like(skiprows):
    exit(cast("int | Sequence[int]", skiprows))
elif skiprows is None:
    exit(0)
raise TypeError(f"{type(skiprows).__name__} is not a valid type for skipping rows")
