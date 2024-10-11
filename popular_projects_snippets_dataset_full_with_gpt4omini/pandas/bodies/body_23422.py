# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Utility to get the values view, mask, dtype, dtype_max, and fill_value.

    If both mask and fill_value/fill_value_typ are not None and skipna is True,
    the values array will be copied.

    For input arrays of boolean or integer dtypes, copies will only occur if a
    precomputed mask, a fill_value/fill_value_typ, and skipna=True are
    provided.

    Parameters
    ----------
    values : ndarray
        input array to potentially compute mask for
    skipna : bool
        boolean for whether NaNs should be skipped
    fill_value : Any
        value to fill NaNs with
    fill_value_typ : str
        Set to '+inf' or '-inf' to handle dtype-specific infinities
    mask : Optional[np.ndarray[bool]]
        nan-mask if known

    Returns
    -------
    values : ndarray
        Potential copy of input value array
    mask : Optional[ndarray[bool]]
        Mask for values, if deemed necessary to compute
    dtype : np.dtype
        dtype for values
    dtype_max : np.dtype
        platform independent dtype
    fill_value : Any
        fill value used
    """
# In _get_values is only called from within nanops, and in all cases
#  with scalar fill_value.  This guarantee is important for the
#  np.where call below
assert is_scalar(fill_value)
# error: Incompatible types in assignment (expression has type "Union[Any,
# Union[ExtensionArray, ndarray]]", variable has type "ndarray")
values = extract_array(values, extract_numpy=True)  # type: ignore[assignment]

mask = _maybe_get_mask(values, skipna, mask)

dtype = values.dtype

datetimelike = False
if needs_i8_conversion(values.dtype):
    # changing timedelta64/datetime64 to int64 needs to happen after
    #  finding `mask` above
    values = np.asarray(values.view("i8"))
    datetimelike = True

dtype_ok = _na_ok_dtype(dtype)

# get our fill value (in case we need to provide an alternative
# dtype for it)
fill_value = _get_fill_value(
    dtype, fill_value=fill_value, fill_value_typ=fill_value_typ
)

if skipna and (mask is not None) and (fill_value is not None):
    if mask.any():
        if dtype_ok or datetimelike:
            values = values.copy()
            np.putmask(values, mask, fill_value)
        else:
            # np.where will promote if needed
            values = np.where(~mask, values, fill_value)

    # return a platform independent precision dtype
dtype_max = dtype
if is_integer_dtype(dtype) or is_bool_dtype(dtype):
    dtype_max = np.dtype(np.int64)
elif is_float_dtype(dtype):
    dtype_max = np.dtype(np.float64)

exit((values, mask, dtype, dtype_max, fill_value))
