# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_tensor(value)
row_partitions = [RowPartition.from_row_splits(x) for x in row_partitions]
expected = DynamicRaggedShape(row_partitions, inner_shape)
self.assertShapeEq(shape, expected)
