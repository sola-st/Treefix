# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(2, 3).astype(np.float32)
    a = constant_op.constant(inp)
    tiled = array_ops.tile(a, [5, 0])
    result = self.evaluate(tiled)
self.assertEqual(result.shape, (10, 0))
self.assertEqual([10, 0], tiled.get_shape())
