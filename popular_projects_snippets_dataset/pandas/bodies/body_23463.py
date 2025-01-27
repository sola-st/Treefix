# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Cumulative function with skipna support.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    accum_func : {np.cumprod, np.maximum.accumulate, np.cumsum, np.minimum.accumulate}
    skipna : bool

    Returns
    -------
    np.ndarray or ExtensionArray
    """
mask_a, mask_b = {
    np.cumprod: (1.0, np.nan),
    np.maximum.accumulate: (-np.inf, np.nan),
    np.cumsum: (0.0, np.nan),
    np.minimum.accumulate: (np.inf, np.nan),
}[accum_func]

# This should go through ea interface
assert values.dtype.kind not in ["m", "M"]

# We will be applying this function to block values
if skipna and not issubclass(values.dtype.type, (np.integer, np.bool_)):
    vals = values.copy()
    mask = isna(vals)
    vals[mask] = mask_a
    result = accum_func(vals, axis=0)
    result[mask] = mask_b
else:
    result = accum_func(values, axis=0)

exit(result)
