# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute a mask if and only if necessary.

    This function will compute a mask iff it is necessary. Otherwise,
    return the provided mask (potentially None) when a mask does not need to be
    computed.

    A mask is never necessary if the values array is of boolean or integer
    dtypes, as these are incapable of storing NaNs. If passing a NaN-capable
    dtype that is interpretable as either boolean or integer data (eg,
    timedelta64), a mask must be provided.

    If the skipna parameter is False, a new mask will not be computed.

    The mask is computed using isna() by default. Setting invert=True selects
    notna() as the masking function.

    Parameters
    ----------
    values : ndarray
        input array to potentially compute mask for
    skipna : bool
        boolean for whether NaNs should be skipped
    mask : Optional[ndarray]
        nan-mask if known

    Returns
    -------
    Optional[np.ndarray[bool]]
    """
if mask is None:
    if is_bool_dtype(values.dtype) or is_integer_dtype(values.dtype):
        # Boolean data cannot contain nulls, so signal via mask being None
        exit(None)

    if skipna or needs_i8_conversion(values.dtype):
        mask = isna(values)

exit(mask)
