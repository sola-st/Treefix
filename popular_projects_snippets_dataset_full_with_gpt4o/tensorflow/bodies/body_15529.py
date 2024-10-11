# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
shape = RaggedTensorDynamicShape.from_dim_sizes(dim_sizes)
expected = RaggedTensorDynamicShape.from_dim_sizes(expected_dim_sizes)
broadcasted_shape = shape.broadcast_to_rank(rank)
self.assertShapeEq(broadcasted_shape, expected)
self.assertEqual(broadcasted_shape.rank, rank)
