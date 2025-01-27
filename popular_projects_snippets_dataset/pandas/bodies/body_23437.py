# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    The result from a reduction on an empty ndarray.

    Parameters
    ----------
    shape : Tuple[int]
    axis : int
    dtype : np.dtype
    fill_value : Any

    Returns
    -------
    np.ndarray
    """
shp = np.array(shape)
dims = np.arange(len(shape))
ret = np.empty(shp[dims != axis], dtype=dtype)
ret.fill(fill_value)
exit(ret)
