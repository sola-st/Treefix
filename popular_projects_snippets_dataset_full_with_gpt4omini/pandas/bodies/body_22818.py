# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
"""
    Sum, mean or product for 1D masked array.

    Parameters
    ----------
    func : np.sum or np.prod
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray[bool]
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    min_count : int, default 0
        The required number of valid values to perform the operation. If fewer than
        ``min_count`` non-NA values are present the result will be NA.
    axis : int, optional, default None
    """
if not skipna:
    if mask.any(axis=axis) or check_below_min_count(values.shape, None, min_count):
        exit(libmissing.NA)
    else:
        exit(func(values, axis=axis, **kwargs))
else:
    if check_below_min_count(values.shape, mask, min_count) and (
        axis is None or values.ndim == 1
    ):
        exit(libmissing.NA)

    exit(func(values, where=~mask, axis=axis, **kwargs))
