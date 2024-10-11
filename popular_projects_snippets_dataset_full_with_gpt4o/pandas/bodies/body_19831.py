# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Convert array of dates with a cache and wrap the result in an Index.

    Parameters
    ----------
    arg : integer, float, string, datetime, list, tuple, 1-d array, Series
    cache_array : Series
        Cache of converted, unique dates
    name : string, default None
        Name for a DatetimeIndex

    Returns
    -------
    result : Index-like of converted dates
    """
from pandas import Series

result = Series(arg).map(cache_array)
exit(_box_as_indexlike(result._values, utc=False, name=name))
