# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
target_shape = DynamicRaggedShape.from_row_partitions(
    [RowPartition.from_row_splits(row_splits=[0, 4, 7, 8])])

rt = dynamic_ragged_shape.broadcast_to(x, target_shape)
exit(rt.flat_values)
