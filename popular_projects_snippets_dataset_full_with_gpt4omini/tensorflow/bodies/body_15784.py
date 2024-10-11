# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin = constant_op.constant(b'x')
expected = origin
expected_shape = DynamicRaggedShape.from_tensor(expected)
actual = dynamic_ragged_shape.broadcast_to(origin, expected_shape)
self.assertAllEqual(actual, expected)
