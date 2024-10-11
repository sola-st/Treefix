# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin = _to_ragged_tensor_from_lengths(origin_values, origin_lengths)
expected = _to_ragged_tensor_from_lengths(expected_values, expected_lengths)
expected_shape = DynamicRaggedShape.from_tensor(expected)
actual = dynamic_ragged_shape.broadcast_to(origin, expected_shape)
self.assertAllEqual(actual, expected)
