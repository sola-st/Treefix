# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape_a = DynamicRaggedShape.from_lengths(x_dims)
shape_b = DynamicRaggedShape.from_lengths(y_dims)
shape_e = DynamicRaggedShape.from_lengths(expected_dims)
[actual, bc_a, bc_b
] = dynamic_ragged_shape.broadcast_dynamic_shape_extended(shape_a, shape_b)
[actual_rev, bc_b_rev, bc_a_rev
] = dynamic_ragged_shape.broadcast_dynamic_shape_extended(shape_b, shape_a)
self.assertShapeEq(actual, shape_e)
self.assertShapeEq(actual_rev, shape_e)

rt_a = _to_prime_tensor_from_lengths(x_dims)
bc_a_actual = bc_a.broadcast(rt_a)
bc_a_actual_rev = bc_a_rev.broadcast(rt_a)
bc_a_expected = dynamic_ragged_shape.broadcast_to(rt_a, shape_e)
self.assertAllEqual(bc_a_expected, bc_a_actual)
self.assertAllEqual(bc_a_expected, bc_a_actual_rev)

rt_b = _to_prime_tensor_from_lengths(y_dims)
bc_b_expected = dynamic_ragged_shape.broadcast_to(rt_b, shape_e)
bc_b_actual = bc_b.broadcast(rt_b)
bc_b_actual_rev = bc_b_rev.broadcast(rt_b)
self.assertAllEqual(bc_b_expected, bc_b_actual)
self.assertAllEqual(bc_b_expected, bc_b_actual_rev)

# This just wraps broadcast_dynamic_shape_extended, so nothing
# deeper is required.
result1 = dynamic_ragged_shape.broadcast_dynamic_shape(shape_a, shape_b)
self.assertShapeEq(shape_e, result1)

# Again, just a wrapper.
result2 = ragged_array_ops.broadcast_dynamic_shape(shape_a, shape_b)
self.assertShapeEq(shape_e, result2)
