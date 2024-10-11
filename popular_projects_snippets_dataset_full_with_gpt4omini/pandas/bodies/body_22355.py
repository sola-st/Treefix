# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    reverse of _ensure_data

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    dtype : np.dtype or ExtensionDtype
    original : AnyArrayLike

    Returns
    -------
    ExtensionArray or np.ndarray
    """
if isinstance(values, ABCExtensionArray) and values.dtype == dtype:
    # Catch DatetimeArray/TimedeltaArray
    exit(values)

if not isinstance(dtype, np.dtype):
    # i.e. ExtensionDtype; note we have ruled out above the possibility
    #  that values.dtype == dtype
    cls = dtype.construct_array_type()

    values = cls._from_sequence(values, dtype=dtype)

else:
    if is_datetime64_dtype(dtype):
        dtype = np.dtype("datetime64[ns]")
    elif is_timedelta64_dtype(dtype):
        dtype = np.dtype("timedelta64[ns]")

    values = values.astype(dtype, copy=False)

exit(values)
