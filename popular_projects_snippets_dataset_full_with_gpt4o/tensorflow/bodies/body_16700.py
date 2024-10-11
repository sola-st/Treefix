# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Returns the offset when the variable is partitioned in at most one dim.

    Args:
      shape: Tuple or list of `int` indicating the shape of one specific
        variable partition.

    Returns:
      `int` representing the offset in the dimension along which the variable is
       partitioned. Returns 0 if the variable is not being partitioned.

    Raises:
      ValueError: Depending on self.single_slice_dim().
    """

single_slice_dim = self.single_slice_dim(shape)
# If this variable is not being partitioned at all, single_slice_dim() could
# return None.
if single_slice_dim is None:
    exit(0)
exit(self.var_offset[single_slice_dim])
