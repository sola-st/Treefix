# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np.random.seed(1618)

# Input shape is unknown.
reduction_axes = [1, 2]
c_unknown = array_ops.placeholder(dtypes.float32)
s_unknown = math_ops.reduce_sum(c_unknown, reduction_axes)
self.assertEqual(tensor_shape.unknown_shape(), s_unknown.get_shape())

np_input = np.random.randn(3, 3, 3)
self._compareAll(np_input, reduction_axes, {c_unknown: np_input})

# Input shape only has known rank.
c_known_rank = array_ops.placeholder(dtypes.float32)
c_known_rank.set_shape(tensor_shape.unknown_shape(rank=3))
s_known_rank = math_ops.reduce_sum(
    c_known_rank, reduction_axes, keepdims=True)
self.assertEqual(3, s_known_rank.get_shape().rank)

np_input = np.random.randn(3, 3, 3)
self._compareAll(np_input, reduction_axes, {c_known_rank: np_input})

# Reduction indices are unknown.
unknown_indices = array_ops.placeholder(dtypes.int32)
c_unknown_indices = constant_op.constant([[10.0], [20.0]])
s_unknown_indices = math_ops.reduce_sum(
    c_unknown_indices, unknown_indices, keepdims=False)
self.assertEqual(tensor_shape.unknown_shape(),
                 s_unknown_indices.get_shape())
s_unknown_indices_keep = math_ops.reduce_sum(
    c_unknown_indices, unknown_indices, keepdims=True)
self.assertEqual(2, s_unknown_indices_keep.get_shape().rank)
