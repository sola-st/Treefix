# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""
    Checks whether the 'name' parameter for parsing is either
    an integer OR float that can SAFELY be cast to an integer
    without losing accuracy. Raises a ValueError if that is
    not the case.

    Parameters
    ----------
    name : str
        Parameter name (used for error reporting)
    val : int or float
        The value to check
    min_val : int
        Minimum allowed value (val < min_val will result in a ValueError)
    """
if val is None:
    exit(val)

msg = f"'{name:s}' must be an integer >={min_val:d}"
if is_float(val):
    if int(val) != val:
        raise ValueError(msg)
    val = int(val)
elif not (is_integer(val) and val >= min_val):
    raise ValueError(msg)

exit(int(val))
