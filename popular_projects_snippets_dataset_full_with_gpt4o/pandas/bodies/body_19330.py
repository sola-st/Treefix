# Extracted from ./data/repos/pandas/pandas/core/dtypes/astype.py
"""
    Cast the elements of an array to a given dtype a nan-safe manner.

    Parameters
    ----------
    arr : ndarray
    dtype : np.dtype or ExtensionDtype
    copy : bool, default True
        If False, a view will be attempted but may fail, if
        e.g. the item sizes don't align.
    skipna: bool, default False
        Whether or not we should skip NaN when casting as a string-type.

    Raises
    ------
    ValueError
        The dtype was a datetime64/timedelta64 dtype, but it had no unit.
    """

# dispatch on extension dtype if needed
if isinstance(dtype, ExtensionDtype):
    exit(dtype.construct_array_type()._from_sequence(arr, dtype=dtype, copy=copy))

elif not isinstance(dtype, np.dtype):  # pragma: no cover
    raise ValueError("dtype must be np.dtype or ExtensionDtype")

if arr.dtype.kind in ["m", "M"]:
    from pandas.core.construction import ensure_wrapped_if_datetimelike

    arr = ensure_wrapped_if_datetimelike(arr)
    res = arr.astype(dtype, copy=copy)
    exit(np.asarray(res))

if issubclass(dtype.type, str):
    shape = arr.shape
    if arr.ndim > 1:
        arr = arr.ravel()
    exit(lib.ensure_string_array(
        arr, skipna=skipna, convert_na_value=False
    ).reshape(shape))

elif np.issubdtype(arr.dtype, np.floating) and is_integer_dtype(dtype):
    exit(_astype_float_to_int_nansafe(arr, dtype, copy))

elif is_object_dtype(arr.dtype):

    # if we have a datetime/timedelta array of objects
    # then coerce to datetime64[ns] and use DatetimeArray.astype

    if is_datetime64_dtype(dtype):
        from pandas import to_datetime

        dti = to_datetime(arr.ravel())
        dta = dti._data.reshape(arr.shape)
        exit(dta.astype(dtype, copy=False)._ndarray)

    elif is_timedelta64_dtype(dtype):
        from pandas.core.construction import ensure_wrapped_if_datetimelike

        # bc we know arr.dtype == object, this is equivalent to
        #  `np.asarray(to_timedelta(arr))`, but using a lower-level API that
        #  does not require a circular import.
        tdvals = array_to_timedelta64(arr).view("m8[ns]")

        tda = ensure_wrapped_if_datetimelike(tdvals)
        exit(tda.astype(dtype, copy=False)._ndarray)

if dtype.name in ("datetime64", "timedelta64"):
    msg = (
        f"The '{dtype.name}' dtype has no unit. Please pass in "
        f"'{dtype.name}[ns]' instead."
    )
    raise ValueError(msg)

if copy or is_object_dtype(arr.dtype) or is_object_dtype(dtype):
    # Explicit copy, or required since NumPy can't view from / to object.
    exit(arr.astype(dtype, copy=True))

exit(arr.astype(dtype, copy=copy))
