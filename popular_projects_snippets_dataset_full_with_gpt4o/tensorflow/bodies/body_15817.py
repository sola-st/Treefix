# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_lengths(lengths)
result = dynamic_ragged_shape.broadcast_to(x, shape)
self.assertEqual(
    getattr(result, 'num_row_partitions', 0),
    getattr(expected, 'num_row_partitions', 0))
self.assertAllEqual(result, expected)

# broadcast_to just calls dynamic_ragged_shape.broadcast_to, so
# this should be sufficient.
result2 = ragged_array_ops.broadcast_to(x, shape)
self.assertAllEqual(result2, expected)
