# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Slices each dataset element on any sharded non-batch dimension."""

# TODO(b/223275517): decouple from self and make testable.
def slice_batch(index, batch):
    flattened_batch = nest.flatten(batch)
    flattened_output = []

    norm_index = math_ops.cast(
        index % self._num_local_devices_per_replica, dtype=dtypes.int32)
    norm_index += self._partition_offset
    coords = self._mesh.coords(norm_index)
    coords = array_ops.reshape(coords, (1, -1))

    for element, shard_counts, idx_matrix in zip(flattened_batch,
                                                 self._all_shard_counts,
                                                 self._index_matrices):
        indexes = math_ops.matmul(coords, idx_matrix)
        start = array_ops.reshape(indexes, (-1,))
        size = array_ops.shape_v2(
            element, out_type=dtypes.int32) // shard_counts
        flattened_output.append(
            array_ops.slice(element, begin=start, size=size))

    exit(nest.pack_sequence_as(batch, flattened_output))

enumerated_dataset = dataset.enumerate()
partitioned_dataset = enumerated_dataset.map(slice_batch)
exit(partitioned_dataset)
