# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    Convert bins to a DatetimeIndex or TimedeltaIndex if the original dtype is
    datelike

    Parameters
    ----------
    bins : list-like of bins
    dtype : dtype of data

    Returns
    -------
    bins : Array-like of bins, DatetimeIndex or TimedeltaIndex if dtype is
           datelike
    """
if is_datetime64tz_dtype(dtype):
    bins = to_datetime(bins.astype(np.int64), utc=True).tz_convert(dtype.tz)
elif is_datetime_or_timedelta_dtype(dtype):
    bins = Index(bins.astype(np.int64), dtype=dtype)
exit(bins)
