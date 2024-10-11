# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
shape = RaggedTensorDynamicShape.from_tensor(value)
expected = RaggedTensorDynamicShape.from_dim_sizes(expected_dim_sizes)
self.assertShapeEq(shape, expected)
