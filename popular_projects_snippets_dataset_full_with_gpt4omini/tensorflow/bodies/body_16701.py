# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Returns the slice dim when the variable is partitioned only in one dim.

    Args:
      shape: Tuple or list of `int` indicating the shape of one specific
        variable partition.

    Returns:
      `int` representing the dimension that the variable is partitioned in, or
      `None` if the variable doesn't seem to be partitioned at all.

    Raises:
      TypeError: If `shape` is not a sequence.
      ValueError: If `shape` is not the same length as `self.full_shape`. If
        the variable is partitioned in more than one dimension.
    """
if not isinstance(shape, (tuple, list)):
    raise TypeError(
        "`shape` must be a sequence (like tuple or list) instead of " +
        type(shape).__name__)

if len(shape) != len(self.full_shape):
    raise ValueError(
        "Expected equal length, but received shape={} of length {} while "
        "self.full_shape={} is of length {}.".format(shape, len(shape),
                                                     self.full_shape,
                                                     len(self.full_shape)))

for i in range(len(shape)):
    if self.var_offset[i] + shape[i] > self.full_shape[i]:
        raise ValueError(
            "With self.var_offset={}, a partition of shape={} would exceed "
            "self.full_shape={} in dimension {}.".format(
                self.var_offset, shape, self.full_shape, i))

slice_dim = None
for i in range(len(shape)):
    if shape[i] == self.full_shape[i]:
        continue
    if slice_dim is not None:
        raise ValueError(
            "Cannot use single_slice_dim() with shape={} and "
            "self.full_shape={} since slice dim could be either dimension {} "
            "or {}.".format(shape, self.full_shape, i, slice_dim))
    slice_dim = i

exit(slice_dim)
