# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape._from_inner_shape([1])
b = DynamicRaggedShape._from_inner_shape([3])
(c, ac, bc) = dynamic_ragged_shape.broadcast_dynamic_shape_extended(a, b)
expected_c = DynamicRaggedShape._from_inner_shape([3])
self.assertShapeEq(c, expected_c)
ac_result = ac.broadcast(constant_op.constant([4]))
self.assertAllEqual(ac_result, [4, 4, 4])
bc_result = bc.broadcast(constant_op.constant([4, 7, 1]))
self.assertAllEqual(bc_result, [4, 7, 1])
