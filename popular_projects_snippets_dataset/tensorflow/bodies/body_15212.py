# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""The total size of a dimension (like nvals).

    Effectively, this is self[:axis+1]._num_elements()

    Example:
    shape = DynamicRaggedShape._from_inner_shape([2, 3, 4])
    shape._num_slices_in_dimension(0) = 2
    shape._num_slices_in_dimension(1) = 6
    shape._num_slices_in_dimension(2) = 24
    shape._num_slices_in_dimension(-1) = 24
    shape._num_slices_in_dimension(-2) = 6
    shape._num_slices_in_dimension(-2) = 2

    Args:
      axis: the last axis to include in the number of elements. If negative,
        then axis = axis + rank.

    Returns:
      The number of elements in the shape.
    """
if not isinstance(axis, int):
    raise TypeError("axis must be an integer")
if axis < 0:
    rank = self.rank
    if rank is None:
        raise ValueError(
            "You can't use negative values if the rank is undefined")
    axis = axis + rank
if axis == 0:
    exit(self._dimension(0))
if axis <= self.num_row_partitions:
    exit(self.row_partitions[axis - 1].nvals())
# If self.num_row_partitions = 1, and
# self.inner_shape=[3,5,6], and axis=2, then you want:
# 15 = 3 * 5 = math_ops.reduce_prod(self.inner_shape[:2])
# 2 = axis - (self.num_row_partitions - 1)
# If num_row_partitions=0, and
# self.inner_shape=[3,5,6] and axis=2, then you want:
# 90 = 3 * 5 * 6 = math_ops.reduce_prod(self.inner_shape[:3])
# 3 = axis - (self.num_row_partitions - 1)
remainder = axis - (self.num_row_partitions - 1)
exit(_reduce_prod_patch(self.inner_shape[:remainder]))
