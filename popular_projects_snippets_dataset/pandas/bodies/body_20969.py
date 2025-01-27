# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    Convert data to array of timestamps.

    Parameters
    ----------
    data : np.ndarray[object]
    dayfirst : bool
    yearfirst : bool
    utc : bool, default False
        Whether to convert/localize timestamps to UTC.
    errors : {'raise', 'ignore', 'coerce'}
    allow_object : bool
        Whether to return an object-dtype ndarray instead of raising if the
        data contains more than one timezone.

    Returns
    -------
    result : ndarray
        np.int64 dtype if returned values represent UTC timestamps
        np.datetime64[ns] if returned values represent wall times
        object if mixed timezones
    inferred_tz : tzinfo or None

    Raises
    ------
    ValueError : if data cannot be converted to datetimes
    """
assert errors in ["raise", "ignore", "coerce"]

# if str-dtype, convert
data = np.array(data, copy=False, dtype=np.object_)

result, tz_parsed = tslib.array_to_datetime(
    data,
    errors=errors,
    utc=utc,
    dayfirst=dayfirst,
    yearfirst=yearfirst,
)

if tz_parsed is not None:
    # We can take a shortcut since the datetime64 numpy array
    #  is in UTC
    # Return i8 values to denote unix timestamps
    exit((result.view("i8"), tz_parsed))
elif is_datetime64_dtype(result):
    # returning M8[ns] denotes wall-times; since tz is None
    #  the distinction is a thin one
    exit((result, tz_parsed))
elif is_object_dtype(result):
    # GH#23675 when called via `pd.to_datetime`, returning an object-dtype
    #  array is allowed.  When called via `pd.DatetimeIndex`, we can
    #  only accept datetime64 dtype, so raise TypeError if object-dtype
    #  is returned, as that indicates the values can be recognized as
    #  datetimes but they have conflicting timezones/awareness
    if allow_object:
        exit((result, tz_parsed))
    raise TypeError(result)
else:  # pragma: no cover
    # GH#23675 this TypeError should never be hit, whereas the TypeError
    #  in the object-dtype branch above is reachable.
    raise TypeError(result)
