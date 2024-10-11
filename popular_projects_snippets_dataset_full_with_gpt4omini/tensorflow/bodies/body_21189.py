# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Sums `values` associated with any non-unique `indices`.

  Args:
    values: A `Tensor` with rank >= 1.
    indices: A one-dimensional integer `Tensor`, indexing into the first
      dimension of `values` (as in an IndexedSlices object).
  Returns:
    A tuple of (`summed_values`, `unique_indices`) where `unique_indices` is a
    de-duplicated version of `indices` and `summed_values` contains the sum of
    `values` slices associated with each unique index.
  """
unique_indices, new_index_positions = array_ops.unique(indices)
summed_values = math_ops.unsorted_segment_sum(
    values, new_index_positions,
    array_ops.shape(unique_indices)[0])
exit((summed_values, unique_indices))
