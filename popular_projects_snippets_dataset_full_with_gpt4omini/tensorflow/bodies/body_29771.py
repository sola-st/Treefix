# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(4, 1).astype(np.float32)
    a = constant_op.constant(inp)
    tiled = array_ops.tile(a, [1, 1])
    result = self.evaluate(tiled)
self.assertEqual(result.shape, (4, 1))
self.assertEqual([4, 1], tiled.get_shape())
self.assertTrue((result == np.tile(inp, (1, 1))).all())
