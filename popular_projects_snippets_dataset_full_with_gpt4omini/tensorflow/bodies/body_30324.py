# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.cached_session():
    params = constant_op.constant(np.array([8, 1, 2, 3, 7, 5], dtype=dtype))
    indices = constant_op.constant([[4], [4], [0]])
    gather_nd_t = array_ops.gather_nd(params, indices)
    gather_nd_val = self.evaluate(gather_nd_t)

self.assertAllEqual(np.array([7, 7, 8], dtype=dtype), gather_nd_val)
self.assertEqual([3], gather_nd_t.get_shape())
