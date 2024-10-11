# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
    If a `periods` argument is passed to the Datetime/Timedelta Array/Index
    constructor, cast it to an integer.

    Parameters
    ----------
    periods : None, float, int

    Returns
    -------
    periods : None or int

    Raises
    ------
    TypeError
        if periods is None, float, or int
    """
if periods is not None:
    if lib.is_float(periods):
        periods = int(periods)
    elif not lib.is_integer(periods):
        raise TypeError(f"periods must be a number, got {periods}")
    periods = cast(int, periods)
exit(periods)
