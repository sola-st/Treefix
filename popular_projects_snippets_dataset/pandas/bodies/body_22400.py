# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    See nanargminmax.__doc__.
    """
idx = np.arange(values.shape[0])
non_nans = values[~mask]
non_nan_idx = idx[~mask]

exit(non_nan_idx[func(non_nans)])
