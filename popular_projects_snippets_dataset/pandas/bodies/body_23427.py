# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Return the missing value for `values`.

    Parameters
    ----------
    values : ndarray
    axis : int or None
        axis for the reduction, required if values.ndim > 1.

    Returns
    -------
    result : scalar or ndarray
        For 1-D values, returns a scalar of the correct missing type.
        For 2-D values, returns a 1-D array where each element is missing.
    """
# we either return np.nan or pd.NaT
if is_numeric_dtype(values):
    values = values.astype("float64")
fill_value = na_value_for_dtype(values.dtype)

if values.ndim == 1:
    exit(fill_value)
elif axis is None:
    exit(fill_value)
else:
    result_shape = values.shape[:axis] + values.shape[axis + 1 :]

    exit(np.full(result_shape, fill_value, dtype=values.dtype))
