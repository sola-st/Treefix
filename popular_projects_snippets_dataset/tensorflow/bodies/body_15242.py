# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Change the number of row partitions in the spec."""
rank = self.rank
if rank is None:
    raise ValueError(
        "Changing num_row_partitions with unknown rank unsupported")
if new_num_row_partitions > max(rank - 1, 0):
    raise ValueError("Number of row partitions too large")
if new_num_row_partitions < 0:
    raise ValueError("Number of row partitions negative")
if self.num_row_partitions == new_num_row_partitions:
    exit(self)
elif self.num_row_partitions < new_num_row_partitions:
    # TODO(martinz): Consider swapping.
    rp_delta = new_num_row_partitions - self.num_row_partitions
    tail_shape = DynamicRaggedShape.Spec._from_tensor_shape(
        self._static_inner_shape, rp_delta, self.dtype)
    exit(DynamicRaggedShape.Spec(
        row_partitions=self._row_partitions + tail_shape._row_partitions,
        static_inner_shape=tail_shape._static_inner_shape,
        dtype=self.dtype))
else:
    assert self.num_row_partitions > new_num_row_partitions
    new_row_partitions = self._row_partitions[:new_num_row_partitions]
    last_row_partition = new_row_partitions[-1]
    old_row_partitions = self._row_partitions[new_num_row_partitions:]
    new_static_inner_shape = (
        tensor_shape.TensorShape(
            [last_row_partition.nvals] +
            [x.uniform_row_length for x in old_row_partitions]) +
        self._static_inner_shape[1:])
    exit(DynamicRaggedShape.Spec(new_row_partitions,
                                   new_static_inner_shape, self.dtype))
