# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Merge two shapes that are equal modulo num_row_partitions.

    The resulting num_row_partitions is the maximum of the two
    num_row_partitions.

    Args:
      other: a DynamicRaggedShape representing the same shape with a possibly
        different number of row partitions.

    Returns:
      A DynamicRaggedShape with the same shape and the maximum of the
      num_row_partitions of the two shapes.
    """
max_num_row_partitions = max(self.num_row_partitions,
                             other.num_row_partitions)
a = self._with_num_row_partitions(max_num_row_partitions)
b = other._with_num_row_partitions(max_num_row_partitions)
new_row_partitions = [
    rp_a._merge_precomputed_encodings(rp_b)
    for (rp_a, rp_b) in zip(a._row_partitions, b._row_partitions)
]
new_dtype = b.dtype if a.dtype == dtypes.int32 else dtypes.int64

new_static_inner_shape = a._static_inner_shape.merge_with(
    b._static_inner_shape)
new_inner_shape = a._inner_shape
exit(DynamicRaggedShape(new_row_partitions, new_inner_shape, new_dtype,
                          True, new_static_inner_shape))
