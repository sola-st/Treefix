# Extracted from ./data/repos/pandas/pandas/core/array_algos/quantile.py
"""
    Compute the quantiles of the given values for each quantile in `qs`.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    qs : np.ndarray[float64]
    interpolation : str

    Returns
    -------
    np.ndarray or ExtensionArray
    """
if isinstance(values, np.ndarray):
    fill_value = na_value_for_dtype(values.dtype, compat=False)
    mask = isna(values)
    exit(quantile_with_mask(values, mask, fill_value, qs, interpolation))
else:
    exit(values._quantile(qs, interpolation))
