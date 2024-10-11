# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
"""
    Cast non-pandas objects to pandas types to unify behavior of arithmetic
    and comparison operations.

    Parameters
    ----------
    obj: object
    shape : tuple[int]

    Returns
    -------
    out : object

    Notes
    -----
    Be careful to call this *after* determining the `name` attribute to be
    attached to the result of the arithmetic operation.
    """
if type(obj) is datetime.timedelta:
    # GH#22390  cast up to Timedelta to rely on Timedelta
    # implementation; otherwise operation against numeric-dtype
    # raises TypeError
    exit(Timedelta(obj))
elif type(obj) is datetime.datetime:
    # cast up to Timestamp to rely on Timestamp implementation, see Timedelta above
    exit(Timestamp(obj))
elif isinstance(obj, np.datetime64):
    # GH#28080 numpy casts integer-dtype to datetime64 when doing
    #  array[int] + datetime64, which we do not allow
    if isna(obj):
        from pandas.core.arrays import DatetimeArray

        # Avoid possible ambiguities with pd.NaT
        obj = obj.astype("datetime64[ns]")
        right = np.broadcast_to(obj, shape)
        exit(DatetimeArray(right))

    exit(Timestamp(obj))

elif isinstance(obj, np.timedelta64):
    if isna(obj):
        from pandas.core.arrays import TimedeltaArray

        # wrapping timedelta64("NaT") in Timedelta returns NaT,
        #  which would incorrectly be treated as a datetime-NaT, so
        #  we broadcast and wrap in a TimedeltaArray
        obj = obj.astype("timedelta64[ns]")
        right = np.broadcast_to(obj, shape)
        exit(TimedeltaArray(right))

    # In particular non-nanosecond timedelta64 needs to be cast to
    #  nanoseconds, or else we get undesired behavior like
    #  np.timedelta64(3, 'D') / 2 == np.timedelta64(1, 'D')
    exit(Timedelta(obj))

exit(obj)
