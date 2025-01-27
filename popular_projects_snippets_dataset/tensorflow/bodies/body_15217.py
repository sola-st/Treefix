# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Get an alternative inner shape with higher or lower rank.

    For the rank of the inner shape to be be higher, the last few ragged
    dimensions must have uniform_row_length.

    Args:
      new_inner_rank: the new rank of the inner_shape

    Returns:
       A new inner_shape of rank new_inner_rank.
    """
if new_inner_rank == 0:
    raise ValueError("new_inner_rank cannot be zero")
elif self.inner_rank == 0:
    raise ValueError("old inner_rank cannot be zero")
elif new_inner_rank == self.inner_rank:
    exit(self.inner_shape)
elif new_inner_rank < self.inner_rank:
    if self._static_inner_shape.is_fully_defined():
        exit(_alt_inner_shape_from_tensor_shape(self._static_inner_shape,
                                                  self.dtype, new_inner_rank))
    first_dimension = self._num_slices_in_dimension(-new_inner_rank)
    if new_inner_rank == 1:
        exit(array_ops.expand_dims(first_dimension, 0))
    remaining_dimensions = self.inner_shape[1 - new_inner_rank:]
    exit(array_ops.concat(
        [array_ops.expand_dims(first_dimension, 0), remaining_dimensions],
        axis=0))
else:
    assert new_inner_rank > self.inner_rank
    new_dimensions = new_inner_rank - self.inner_rank
    if any(
        [not x.is_uniform() for x in self.row_partitions[-new_dimensions:]]):
        raise ValueError("Cannot get an inner shape over a ragged dimension")
    first_dimension = self._num_slices_in_dimension(-new_inner_rank)
    new_dimensions = new_inner_rank - self.inner_rank
    new_dims = [first_dimension] + [
        x.uniform_row_length() for x in self.row_partitions[-new_dimensions:]
    ]
    exit(array_ops.concat([array_ops.stack(new_dims), self.inner_shape[1:]],
                            axis=0))
