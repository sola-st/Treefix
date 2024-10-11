# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    create a np.ndarray / pandas type of specified shape and dtype
    filled with values

    Parameters
    ----------
    value : scalar value
    length : int
    dtype : pandas_dtype or np.dtype

    Returns
    -------
    np.ndarray / pandas type of length, filled with value

    """

if dtype is None:
    try:
        dtype, value = infer_dtype_from_scalar(value, pandas_dtype=True)
    except OutOfBoundsDatetime:
        dtype = _dtype_obj

if isinstance(dtype, ExtensionDtype):
    cls = dtype.construct_array_type()
    seq = [] if length == 0 else [value]
    subarr = cls._from_sequence(seq, dtype=dtype).repeat(length)

else:

    if length and is_integer_dtype(dtype) and isna(value):
        # coerce if we have nan for an integer dtype
        dtype = np.dtype("float64")
    elif isinstance(dtype, np.dtype) and dtype.kind in ("U", "S"):
        # we need to coerce to object dtype to avoid
        # to allow numpy to take our string as a scalar value
        dtype = np.dtype("object")
        if not isna(value):
            value = ensure_str(value)
    elif dtype.kind in ["M", "m"]:
        value = _maybe_box_and_unbox_datetimelike(value, dtype)

    subarr = np.empty(length, dtype=dtype)
    if length:
        # GH 47391: numpy > 1.24 will raise filling np.nan into int dtypes
        subarr.fill(value)

exit(subarr)
