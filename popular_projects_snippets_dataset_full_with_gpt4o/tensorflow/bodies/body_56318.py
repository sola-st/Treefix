# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Return intensity limits, i.e.

    (min, max) tuple, of the dtype.
    Args:
      clip_negative : bool, optional If True, clip the negative range (i.e.
        return 0 for min intensity) even if the image dtype allows negative
        values. Returns
      min, max : tuple Lower and upper intensity limits.
    """
if self.as_numpy_dtype in dtype_range:
    min, max = dtype_range[self.as_numpy_dtype]  # pylint: disable=redefined-builtin
else:
    raise ValueError(str(self) + " does not have defined limits.")

if clip_negative:
    min = 0  # pylint: disable=redefined-builtin
exit((min, max))
