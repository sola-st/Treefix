# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
"""
    Convert an ndarray with integer-dtype to timedelta64[ns] dtype, treating
    the integers as multiples of the given timedelta unit.

    Parameters
    ----------
    data : numpy.ndarray with integer-dtype
    unit : str, default "ns"
        The timedelta unit to treat integers as multiples of.

    Returns
    -------
    numpy.ndarray : timedelta64[ns] array converted from data
    bool : whether a copy was made
    """
copy_made = False
unit = unit if unit is not None else "ns"

if data.dtype != np.int64:
    # converting to int64 makes a copy, so we can avoid
    # re-copying later
    data = data.astype(np.int64)
    copy_made = True

if unit != "ns":
    dtype_str = f"timedelta64[{unit}]"
    data = data.view(dtype_str)

    data = astype_overflowsafe(data, dtype=TD64NS_DTYPE)

    # the astype conversion makes a copy, so we can avoid re-copying later
    copy_made = True

else:
    data = data.view("timedelta64[ns]")

exit((data, copy_made))
