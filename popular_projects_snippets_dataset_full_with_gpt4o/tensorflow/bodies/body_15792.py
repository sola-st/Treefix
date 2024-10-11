# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin = constant_op.constant(origin)
expected_shape = DynamicRaggedShape.from_lengths(expected_lengths)
if expected_num_row_partitions is not None:
    expected_shape = expected_shape._with_num_row_partitions(
        expected_num_row_partitions)
expected = ragged_factory_ops.constant_value(expected)
actual = dynamic_ragged_shape.broadcast_to(origin, expected_shape)
self.assertAllEqual(actual, expected)
