# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_accumulations.py
"""
    Accumulations for 1D masked array.

    We will modify values in place to replace NAs with the appropriate fill value.

    Parameters
    ----------
    func : np.cumsum, np.cumprod, np.maximum.accumulate, np.minimum.accumulate
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    """
dtype_info: np.iinfo | np.finfo
if is_float_dtype(values):
    dtype_info = np.finfo(values.dtype.type)
elif is_integer_dtype(values):
    dtype_info = np.iinfo(values.dtype.type)
elif is_bool_dtype(values):
    # Max value of bool is 1, but since we are setting into a boolean
    # array, 255 is fine as well. Min value has to be 0 when setting
    # into the boolean array.
    dtype_info = np.iinfo(np.uint8)
else:
    raise NotImplementedError(
        f"No masked accumulation defined for dtype {values.dtype.type}"
    )
try:
    fill_value = {
        np.cumprod: 1,
        np.maximum.accumulate: dtype_info.min,
        np.cumsum: 0,
        np.minimum.accumulate: dtype_info.max,
    }[func]
except KeyError:
    raise NotImplementedError(
        f"No accumulation for {func} implemented on BaseMaskedArray"
    )

values[mask] = fill_value

if not skipna:
    mask = np.maximum.accumulate(mask)

values = func(values)
exit((values, mask))
