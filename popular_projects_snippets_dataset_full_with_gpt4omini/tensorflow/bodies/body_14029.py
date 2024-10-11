# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
rt = ragged_factory_ops.constant(rt, rt_ragged_rank)
partitions = structured_tensor._row_partitions_for_ragged_tensor(
    rt, rank, dtypes.int64)
self.assertLen(partitions, rank - 1)
self.assertLen(partitions, len(expected_row_lengths))
for partition, expected in zip(partitions, expected_row_lengths):
    self.assertAllEqual(partition.row_lengths(), expected)
