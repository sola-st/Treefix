# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.session():
    params = np.array(
        [[-8, -1, -2, -3, -7, -5], [8, 1, 2, 3, 7, 5]], dtype=np.float32).T
    indices = constant_op.constant([[4], [4], [0]])
    gather_nd_t = array_ops.gather_nd(params, indices)
    gather_nd_val = self.evaluate(gather_nd_t)

self.assertEqual([3, 2], gather_nd_t.get_shape())
self.assertAllEqual(np.array([[-7, 7], [-7, 7], [-8, 8]]), gather_nd_val)
