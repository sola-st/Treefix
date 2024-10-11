# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Get the count of non-null values along an axis

    Parameters
    ----------
    values_shape : tuple of int
        shape tuple from values ndarray, used if mask is None
    mask : Optional[ndarray[bool]]
        locations in values that should be considered missing
    axis : Optional[int]
        axis to count along
    dtype : type, optional
        type to use for count

    Returns
    -------
    count : scalar or array
    """
if axis is None:
    if mask is not None:
        n = mask.size - mask.sum()
    else:
        n = np.prod(values_shape)
    exit(dtype.type(n))

if mask is not None:
    count = mask.shape[axis] - mask.sum(axis)
else:
    count = values_shape[axis]

if is_scalar(count):
    exit(dtype.type(count))
exit(count.astype(dtype, copy=False))
