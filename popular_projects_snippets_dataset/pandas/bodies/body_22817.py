# Extracted from ./data/repos/pandas/pandas/core/array_algos/putmask.py
"""
    Parameters
    ----------
    values : np.ndarray
    num_set : int
        For putmask, this is mask.sum()
    other : Any
    """
if values.dtype == object:
    dtype, _ = infer_dtype_from(other, pandas_dtype=True)

    if isinstance(dtype, np.dtype) and dtype.kind in ["m", "M"]:
        # https://github.com/numpy/numpy/issues/12550
        #  timedelta64 will incorrectly cast to int
        if not is_list_like(other):
            other = [other] * num_set
        else:
            other = list(other)

exit(other)
