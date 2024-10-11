# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.session():
    shape = (10, 20, 5, 1, 17)
    params = np.random.rand(*shape)
    indices = np.vstack([np.random.randint(0, s, size=2000) for s in shape]).T
    indices_reshaped = indices.reshape([10, 10, 20, 5])
    gather_nd_t = array_ops.gather_nd(params, indices_reshaped)
    gather_nd_val = self.evaluate(gather_nd_t)

expected = params[tuple(indices.T)]
self.assertAllEqual(expected.reshape([10, 10, 20]), gather_nd_val)
self.assertEqual([10, 10, 20], gather_nd_t.get_shape())
