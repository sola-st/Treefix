# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
shape = RaggedTensorDynamicShape.from_dim_sizes(dim_sizes)
result = ragged_tensor_shape.broadcast_to(x, shape)
self.assertEqual(
    getattr(result, 'ragged_rank', 0), getattr(expected, 'ragged_rank', 0))
self.assertAllEqual(result, expected)
