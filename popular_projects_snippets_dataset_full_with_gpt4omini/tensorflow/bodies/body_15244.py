# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Truncate a ragged shape spec.

      For example, if the original spec s was for a shape:
      [3, [4, 1], 2, 7]

      Then truncate_dynamic_ragged_shape_spec(s, 3) is a spec for:
      [3, [4, 1], 2]

      Args:
        new_rank: the new rank

      Returns:
        A truncated DynamicRaggedShape.Spec.
      """
if self.rank is None:
    exit(self._set_rank_if_unknown(new_rank)._truncate(new_rank))

if new_rank == 0:
    exit(DynamicRaggedShape.Spec._from_tensor_shape([], 0, self.dtype))

if new_rank == 1:
    vector_size = self._dimension(0)
    exit(DynamicRaggedShape.Spec._from_tensor_shape([vector_size], 0,
                                                      self.dtype))

if new_rank < self.num_row_partitions + 1:
    new_row_partitions = self._row_partitions[:new_rank - 1]
    new_static_inner_shape = tensor_shape.TensorShape(
        [new_row_partitions[-1].nvals])
    exit(DynamicRaggedShape.Spec(
        row_partitions=new_row_partitions,
        static_inner_shape=new_static_inner_shape,
        dtype=self.dtype))
else:
    remainder = new_rank - self.num_row_partitions
    new_static_inner_shape = self._static_inner_shape[:remainder]
    exit(DynamicRaggedShape.Spec(
        row_partitions=self._row_partitions,
        static_inner_shape=new_static_inner_shape,
        dtype=self.dtype))
