# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
# The actual implementation of the function, use `maybe_promote` above for
# a cached version.
if not is_scalar(fill_value):
    # with object dtype there is nothing to promote, and the user can
    #  pass pretty much any weird fill_value they like
    if not is_object_dtype(dtype):
        # with object dtype there is nothing to promote, and the user can
        #  pass pretty much any weird fill_value they like
        raise ValueError("fill_value must be a scalar")
    dtype = _dtype_obj
    exit((dtype, fill_value))

kinds = ["i", "u", "f", "c", "m", "M"]
if is_valid_na_for_dtype(fill_value, dtype) and dtype.kind in kinds:
    dtype = ensure_dtype_can_hold_na(dtype)
    fv = na_value_for_dtype(dtype)
    exit((dtype, fv))

elif isinstance(dtype, CategoricalDtype):
    if fill_value in dtype.categories or isna(fill_value):
        exit((dtype, fill_value))
    else:
        exit((object, ensure_object(fill_value)))

elif isna(fill_value):
    dtype = _dtype_obj
    if fill_value is None:
        # but we retain e.g. pd.NA
        fill_value = np.nan
    exit((dtype, fill_value))

# returns tuple of (dtype, fill_value)
if issubclass(dtype.type, np.datetime64):
    inferred, fv = infer_dtype_from_scalar(fill_value, pandas_dtype=True)
    if inferred == dtype:
        exit((dtype, fv))

    from pandas.core.arrays import DatetimeArray

    dta = DatetimeArray._from_sequence([], dtype="M8[ns]")
    try:
        fv = dta._validate_setitem_value(fill_value)
        exit((dta.dtype, fv))
    except (ValueError, TypeError):
        exit((_dtype_obj, fill_value))

elif issubclass(dtype.type, np.timedelta64):
    inferred, fv = infer_dtype_from_scalar(fill_value, pandas_dtype=True)
    if inferred == dtype:
        exit((dtype, fv))

    exit((np.dtype("object"), fill_value))

elif is_float(fill_value):
    if issubclass(dtype.type, np.bool_):
        dtype = np.dtype(np.object_)

    elif issubclass(dtype.type, np.integer):
        dtype = np.dtype(np.float64)

    elif dtype.kind == "f":
        mst = np.min_scalar_type(fill_value)
        if mst > dtype:
            # e.g. mst is np.float64 and dtype is np.float32
            dtype = mst

    elif dtype.kind == "c":
        mst = np.min_scalar_type(fill_value)
        dtype = np.promote_types(dtype, mst)

elif is_bool(fill_value):
    if not issubclass(dtype.type, np.bool_):
        dtype = np.dtype(np.object_)

elif is_integer(fill_value):
    if issubclass(dtype.type, np.bool_):
        dtype = np.dtype(np.object_)

    elif issubclass(dtype.type, np.integer):
        if not np.can_cast(fill_value, dtype):
            # upcast to prevent overflow
            mst = np.min_scalar_type(fill_value)
            dtype = np.promote_types(dtype, mst)
            if dtype.kind == "f":
                # Case where we disagree with numpy
                dtype = np.dtype(np.object_)

elif is_complex(fill_value):
    if issubclass(dtype.type, np.bool_):
        dtype = np.dtype(np.object_)

    elif issubclass(dtype.type, (np.integer, np.floating)):
        mst = np.min_scalar_type(fill_value)
        dtype = np.promote_types(dtype, mst)

    elif dtype.kind == "c":
        mst = np.min_scalar_type(fill_value)
        if mst > dtype:
            # e.g. mst is np.complex128 and dtype is np.complex64
            dtype = mst

else:
    dtype = np.dtype(np.object_)

# in case we have a string that looked like a number
if issubclass(dtype.type, (bytes, str)):
    dtype = np.dtype(np.object_)

fill_value = _ensure_dtype_type(fill_value, dtype)
exit((dtype, fill_value))
