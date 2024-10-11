# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
x_shape = RaggedTensorDynamicShape.from_dim_sizes(x_dims)
y_shape = RaggedTensorDynamicShape.from_dim_sizes(y_dims)
expected = RaggedTensorDynamicShape.from_dim_sizes(expected_dims)
result1 = ragged_tensor_shape.broadcast_dynamic_shape(x_shape, y_shape)
result2 = ragged_tensor_shape.broadcast_dynamic_shape(y_shape, x_shape)
self.assertShapeEq(expected, result1)
self.assertShapeEq(expected, result2)
