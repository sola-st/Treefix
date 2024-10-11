# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
s_left = DynamicRaggedShape._from_inner_shape(
    constant_op.constant([4, 1], dtype_left))
s_right = DynamicRaggedShape._from_inner_shape(
    constant_op.constant([1, 4], dtype_right))
s_result = dynamic_ragged_shape.broadcast_dynamic_shape(s_left, s_right)
self.assertEqual(s_result.dtype, dtypes.int64)
