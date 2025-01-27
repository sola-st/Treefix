# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Tests broadcast_to on a single dimension."""
original_rt = _to_prime_tensor_from_lengths(original_lengths)
bcast_shape = DynamicRaggedShape.from_lengths(broadcast_lengths)
result_rt = dynamic_ragged_shape.broadcast_to(original_rt, bcast_shape)
result_shape = DynamicRaggedShape.from_tensor(result_rt)

self.assertShapeEq(bcast_shape, result_shape)
