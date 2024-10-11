# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
rt = ragged_tensor.RaggedTensor.from_value_rowids(
    array_ops.constant([[1, 2], [3, 4], [5, 6]]), [0, 0, 1])
struct = StructuredTensor.from_fields({"r": rt}, [2])
struct_2 = struct.partition_outer_dimension(
    row_partition.RowPartition.from_row_splits([0, 1, 2]))
struct_3 = struct_2.partition_outer_dimension(
    row_partition.RowPartition.from_row_splits([0, 1, 2]))
self.assertLen(struct_3.row_partitions, 2)
merged = struct_3.merge_dims(0, 1)
self.assertLen(merged.row_partitions, 1)
