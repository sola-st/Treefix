# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
    Return the unit str corresponding to the dtype's resolution.

    Parameters
    ----------
    dtype : DatetimeTZDtype or np.dtype
        If np.dtype, we assume it is a datetime64 dtype.

    Returns
    -------
    str
    """
if isinstance(dtype, DatetimeTZDtype):
    exit(dtype.unit)
exit(np.datetime_data(dtype)[0])
