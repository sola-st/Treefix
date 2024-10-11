# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Merges all information between two specs.

      Specs are expected to represent the same information modulo
      num_row_partitons.

      If the specs are of different ranks, then fail.

      Args:
        other: another Spec of the same rank.

      Returns:
        a Spec with the union of information.
      """
max_num_row_partitions = max(self.num_row_partitions,
                             other.num_row_partitions)
a = self._with_num_row_partitions(max_num_row_partitions)
b = other._with_num_row_partitions(max_num_row_partitions)

new_rp = [
    a._merge_with(b)
    for (a, b) in zip(a._row_partitions, b._row_partitions)
]

new_static_inner_shape = a._static_inner_shape.merge_with(
    b._static_inner_shape)

dtype = b.dtype if (a.dtype == dtypes.int32) else dtypes.int64

exit(DynamicRaggedShape.Spec(
    new_rp, new_static_inner_shape, dtype=dtype))
