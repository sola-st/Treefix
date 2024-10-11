# Extracted from ./data/repos/pandas/pandas/core/arrays/boolean.py
"""
    Coerce the input values array to numpy arrays with a mask.

    Parameters
    ----------
    values : 1D list-like
    mask : bool 1D array, optional
    copy : bool, default False
        if True, copy the input

    Returns
    -------
    tuple of (values, mask)
    """
if isinstance(values, BooleanArray):
    if mask is not None:
        raise ValueError("cannot pass mask for BooleanArray input")
    values, mask = values._data, values._mask
    if copy:
        values = values.copy()
        mask = mask.copy()
    exit((values, mask))

mask_values = None
if isinstance(values, np.ndarray) and values.dtype == np.bool_:
    if copy:
        values = values.copy()
elif isinstance(values, np.ndarray) and is_numeric_dtype(values.dtype):
    mask_values = isna(values)

    values_bool = np.zeros(len(values), dtype=bool)
    values_bool[~mask_values] = values[~mask_values].astype(bool)

    if not np.all(
        values_bool[~mask_values].astype(values.dtype) == values[~mask_values]
    ):
        raise TypeError("Need to pass bool-like values")

    values = values_bool
else:
    values_object = np.asarray(values, dtype=object)

    inferred_dtype = lib.infer_dtype(values_object, skipna=True)
    integer_like = ("floating", "integer", "mixed-integer-float")
    if inferred_dtype not in ("boolean", "empty") + integer_like:
        raise TypeError("Need to pass bool-like values")

    # mypy does not narrow the type of mask_values to npt.NDArray[np.bool_]
    # within this branch, it assumes it can also be None
    mask_values = cast("npt.NDArray[np.bool_]", isna(values_object))
    values = np.zeros(len(values), dtype=bool)
    values[~mask_values] = values_object[~mask_values].astype(bool)

    # if the values were integer-like, validate it were actually 0/1's
    if (inferred_dtype in integer_like) and not (
        np.all(
            values[~mask_values].astype(float)
            == values_object[~mask_values].astype(float)
        )
    ):
        raise TypeError("Need to pass bool-like values")

if mask is None and mask_values is None:
    mask = np.zeros(values.shape, dtype=bool)
elif mask is None:
    mask = mask_values
else:
    if isinstance(mask, np.ndarray) and mask.dtype == np.bool_:
        if mask_values is not None:
            mask = mask | mask_values
        else:
            if copy:
                mask = mask.copy()
    else:
        mask = np.array(mask, dtype=bool)
        if mask_values is not None:
            mask = mask | mask_values

if values.shape != mask.shape:
    raise ValueError("values.shape and mask.shape must match")

exit((values, mask))
