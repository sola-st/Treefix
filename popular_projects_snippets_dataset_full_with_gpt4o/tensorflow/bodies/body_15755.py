# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if callable(row_partitions):
    row_partitions = row_partitions()
shape = DynamicRaggedShape.from_lengths(
    lengths, num_row_partitions=num_row_partitions)
expected = DynamicRaggedShape(row_partitions, inner_shape)
self.assertShapeEq(shape, expected)
