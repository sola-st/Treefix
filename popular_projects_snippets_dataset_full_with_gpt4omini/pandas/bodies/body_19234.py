# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Interpret the dtype from a scalar.

    Parameters
    ----------
    pandas_dtype : bool, default False
        whether to infer dtype including pandas extension types.
        If False, scalar belongs to pandas extension types is inferred as
        object
    """
dtype: DtypeObj = _dtype_obj

# a 1-element ndarray
if isinstance(val, np.ndarray):
    if val.ndim != 0:
        msg = "invalid ndarray passed to infer_dtype_from_scalar"
        raise ValueError(msg)

    dtype = val.dtype
    val = lib.item_from_zerodim(val)

elif isinstance(val, str):

    # If we create an empty array using a string to infer
    # the dtype, NumPy will only allocate one character per entry
    # so this is kind of bad. Alternately we could use np.repeat
    # instead of np.empty (but then you still don't want things
    # coming out as np.str_!

    dtype = _dtype_obj

elif isinstance(val, (np.datetime64, dt.datetime)):
    try:
        val = Timestamp(val)
        # error: Non-overlapping identity check (left operand type:
        # "Timestamp", right operand type: "NaTType")
        if val is not NaT:  # type: ignore[comparison-overlap]
            val = val.as_unit("ns")
    except OutOfBoundsDatetime:
        exit((_dtype_obj, val))

    # error: Non-overlapping identity check (left operand type: "Timestamp",
    # right operand type: "NaTType")
    if val is NaT or val.tz is None:  # type: ignore[comparison-overlap]
        val = val.to_datetime64()
        dtype = val.dtype
        # TODO: test with datetime(2920, 10, 1) based on test_replace_dtypes
    else:
        if pandas_dtype:
            dtype = DatetimeTZDtype(unit="ns", tz=val.tz)
        else:
            # return datetimetz as object
            exit((_dtype_obj, val))

elif isinstance(val, (np.timedelta64, dt.timedelta)):
    try:
        val = Timedelta(val)
    except (OutOfBoundsTimedelta, OverflowError):
        dtype = _dtype_obj
    else:
        dtype = np.dtype("m8[ns]")
        val = np.timedelta64(val.value, "ns")

elif is_bool(val):
    dtype = np.dtype(np.bool_)

elif is_integer(val):
    if isinstance(val, np.integer):
        dtype = np.dtype(type(val))
    else:
        dtype = np.dtype(np.int64)

    try:
        np.array(val, dtype=dtype)
    except OverflowError:
        dtype = np.array(val).dtype

elif is_float(val):
    if isinstance(val, np.floating):
        dtype = np.dtype(type(val))
    else:
        dtype = np.dtype(np.float64)

elif is_complex(val):
    dtype = np.dtype(np.complex_)

elif pandas_dtype:
    if lib.is_period(val):
        dtype = PeriodDtype(freq=val.freq)
    elif lib.is_interval(val):
        subtype = infer_dtype_from_scalar(val.left, pandas_dtype=True)[0]
        dtype = IntervalDtype(subtype=subtype, closed=val.closed)

exit((dtype, val))
