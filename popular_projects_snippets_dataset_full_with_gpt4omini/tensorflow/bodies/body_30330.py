# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.session():
    params = np.array(
        [[[-8, -1, -2, -3, -7, -5], [8, 1, 2, 3, 7, 5]],
         [[-80, -10, -20, -30, -70, -50], [80, 10, 20, 30, 70, 50]]],
        dtype=np.float32).T
    params_t = constant_op.constant(params)
    indices = constant_op.constant([[4], [4], [0]])
    gather_nd_t = array_ops.gather_nd(params_t, indices)
    gather_nd_val = self.evaluate(gather_nd_t)

self.assertEqual([3, 2, 2], gather_nd_t.get_shape())
self.assertAllEqual(params[[4, 4, 0]], gather_nd_val)
