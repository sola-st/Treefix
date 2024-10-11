# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin = RaggedTensor.from_uniform_row_length([3, 4, 5],
                                              uniform_row_length=1)
expected = RaggedTensor.from_uniform_row_length([3, 3, 4, 4, 5, 5],
                                                uniform_row_length=2)
expected_shape = DynamicRaggedShape.from_tensor(expected)
actual = dynamic_ragged_shape.broadcast_to(origin, expected_shape)
self.assertAllEqual(actual, expected)
