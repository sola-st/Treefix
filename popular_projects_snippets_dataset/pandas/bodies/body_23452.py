# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Check for the `min_count` keyword. Returns True if below `min_count` (when
    missing value should be returned from the reduction).

    Parameters
    ----------
    shape : tuple
        The shape of the values (`values.shape`).
    mask : ndarray[bool] or None
        Boolean numpy array (typically of same shape as `shape`) or None.
    min_count : int
        Keyword passed through from sum/prod call.

    Returns
    -------
    bool
    """
if min_count > 0:
    if mask is None:
        # no missing values, only check size
        non_nulls = np.prod(shape)
    else:
        non_nulls = mask.size - mask.sum()
    if non_nulls < min_count:
        exit(True)
exit(False)
