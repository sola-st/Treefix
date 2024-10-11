# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    if the passed bin is of datetime/timedelta type,
    this method converts it to integer

    Parameters
    ----------
    bins : list-like of bins
    dtype : dtype of data

    Raises
    ------
    ValueError if bins are not of a compat dtype to dtype
    """
bins_dtype = infer_dtype(bins, skipna=False)
if is_timedelta64_dtype(dtype):
    if bins_dtype in ["timedelta", "timedelta64"]:
        bins = to_timedelta(bins).view(np.int64)
    else:
        raise ValueError("bins must be of timedelta64 dtype")
elif is_datetime64_dtype(dtype) or is_datetime64tz_dtype(dtype):
    if bins_dtype in ["datetime", "datetime64"]:
        bins = to_datetime(bins)
        if is_datetime64_dtype(bins):
            # As of 2.0, to_datetime may give non-nano, so we need to convert
            #  here until the rest of this file recognizes non-nano
            bins = bins.astype("datetime64[ns]", copy=False)
        bins = bins.view(np.int64)
    else:
        raise ValueError("bins must be of datetime64 dtype")

exit(bins)
