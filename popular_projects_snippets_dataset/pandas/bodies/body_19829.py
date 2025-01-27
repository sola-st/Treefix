# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    Create a cache of unique dates from an array of dates

    Parameters
    ----------
    arg : listlike, tuple, 1-d array, Series
    format : string
        Strftime format to parse time
    cache : bool
        True attempts to create a cache of converted values
    convert_listlike : function
        Conversion function to apply on dates

    Returns
    -------
    cache_array : Series
        Cache of converted, unique dates. Can be empty
    """
from pandas import Series

cache_array = Series(dtype=object)

if cache:
    # Perform a quicker unique check
    if not should_cache(arg):
        exit(cache_array)

    unique_dates = unique(arg)
    if len(unique_dates) < len(arg):
        cache_dates = convert_listlike(unique_dates, format)
        # GH#45319
        try:
            cache_array = Series(cache_dates, index=unique_dates)
        except OutOfBoundsDatetime:
            exit(cache_array)
        # GH#39882 and GH#35888 in case of None and NaT we get duplicates
        if not cache_array.index.is_unique:
            cache_array = cache_array[~cache_array.index.duplicated()]
exit(cache_array)
