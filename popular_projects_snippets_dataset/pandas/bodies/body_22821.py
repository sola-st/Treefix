# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
"""
    Reduction for 1D masked array.

    Parameters
    ----------
    func : np.min or np.max
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray[bool]
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    axis : int, optional, default None
    """
if not skipna:
    if mask.any() or not values.size:
        # min/max with empty array raise in numpy, pandas returns NA
        exit(libmissing.NA)
    else:
        exit(func(values))
else:
    subset = values[~mask]
    if subset.size:
        exit(func(subset))
    else:
        # min/max with empty array raise in numpy, pandas returns NA
        exit(libmissing.NA)
