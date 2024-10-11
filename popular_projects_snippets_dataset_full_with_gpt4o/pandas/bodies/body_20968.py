# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
    Parameters
    ----------
    data : list-like
    copy : bool, default False
    tz : tzinfo or None, default None
    dayfirst : bool, default False
    yearfirst : bool, default False
    ambiguous : str, bool, or arraylike, default 'raise'
        See pandas._libs.tslibs.tzconversion.tz_localize_to_utc.

    Returns
    -------
    result : numpy.ndarray
        The sequence converted to a numpy array with dtype ``datetime64[ns]``.
    tz : tzinfo or None
        Either the user-provided tzinfo or one inferred from the data.
    inferred_freq : Tick or None
        The inferred frequency of the sequence.

    Raises
    ------
    TypeError : PeriodDType data is passed
    """
inferred_freq = None

data, copy = dtl.ensure_arraylike_for_datetimelike(
    data, copy, cls_name="DatetimeArray"
)

if isinstance(data, DatetimeArray):
    inferred_freq = data.freq

# By this point we are assured to have either a numpy array or Index
data, copy = maybe_convert_dtype(data, copy, tz=tz)
data_dtype = getattr(data, "dtype", None)

if (
    is_object_dtype(data_dtype)
    or is_string_dtype(data_dtype)
    or is_sparse(data_dtype)
):
    # TODO: We do not have tests specific to string-dtypes,
    #  also complex or categorical or other extension
    copy = False
    if lib.infer_dtype(data, skipna=False) == "integer":
        data = data.astype(np.int64)
    elif tz is not None and ambiguous == "raise":
        # TODO: yearfirst/dayfirst/etc?
        obj_data = np.asarray(data, dtype=object)
        i8data = tslib.array_to_datetime_with_tz(obj_data, tz)
        exit((i8data.view(DT64NS_DTYPE), tz, None))
    else:
        # data comes back here as either i8 to denote UTC timestamps
        #  or M8[ns] to denote wall times
        data, inferred_tz = objects_to_datetime64ns(
            data,
            dayfirst=dayfirst,
            yearfirst=yearfirst,
            allow_object=False,
        )
        if tz and inferred_tz:
            #  two timezones: convert to intended from base UTC repr
            if data.dtype == "i8":
                # GH#42505
                # by convention, these are _already_ UTC, e.g
                exit((data.view(DT64NS_DTYPE), tz, None))

            if timezones.is_utc(tz):
                # Fastpath, avoid copy made in tzconversion
                utc_vals = data.view("i8")
            else:
                utc_vals = tz_convert_from_utc(data.view("i8"), tz)
            data = utc_vals.view(DT64NS_DTYPE)
        elif inferred_tz:
            tz = inferred_tz

    data_dtype = data.dtype

# `data` may have originally been a Categorical[datetime64[ns, tz]],
# so we need to handle these types.
if is_datetime64tz_dtype(data_dtype):
    # DatetimeArray -> ndarray
    tz = _maybe_infer_tz(tz, data.tz)
    result = data._ndarray

elif is_datetime64_dtype(data_dtype):
    # tz-naive DatetimeArray or ndarray[datetime64]
    data = getattr(data, "_ndarray", data)
    new_dtype = data.dtype
    data_unit = get_unit_from_dtype(new_dtype)
    if not is_supported_unit(data_unit):
        # Cast to the nearest supported unit, generally "s"
        new_reso = get_supported_reso(data_unit)
        new_unit = npy_unit_to_abbrev(new_reso)
        new_dtype = np.dtype(f"M8[{new_unit}]")
        data = astype_overflowsafe(data, dtype=new_dtype, copy=False)
        data_unit = get_unit_from_dtype(new_dtype)
        copy = False

    if data.dtype.byteorder == ">":
        # TODO: better way to handle this?  non-copying alternative?
        #  without this, test_constructor_datetime64_bigendian fails
        data = data.astype(data.dtype.newbyteorder("<"))
        new_dtype = data.dtype
        copy = False

    if tz is not None:
        # Convert tz-naive to UTC
        # TODO: if tz is UTC, are there situations where we *don't* want a
        #  copy?  tz_localize_to_utc always makes one.
        shape = data.shape
        if data.ndim > 1:
            data = data.ravel()

        data = tzconversion.tz_localize_to_utc(
            data.view("i8"), tz, ambiguous=ambiguous, creso=data_unit
        )
        data = data.view(new_dtype)
        data = data.reshape(shape)

    assert data.dtype == new_dtype, data.dtype
    result = data

else:
    # must be integer dtype otherwise
    # assume this data are epoch timestamps
    if data.dtype != INT64_DTYPE:
        data = data.astype(np.int64, copy=False)
    result = data.view(DT64NS_DTYPE)

if copy:
    result = result.copy()

assert isinstance(result, np.ndarray), type(result)
assert result.dtype.kind == "M"
assert result.dtype != "M8"
assert is_supported_unit(get_unit_from_dtype(result.dtype))
exit((result, tz, inferred_freq))
