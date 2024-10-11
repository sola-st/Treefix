# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# multiples could be int32 or int64
for dtype in [dtypes.int32, dtypes.int64]:
    with self.cached_session():
        inp = np.random.rand(4, 1).astype(np.float32)
        a = constant_op.constant(inp)
        tiled = array_ops.tile(a, constant_op.constant([1, 4], dtype=dtype))
        result = self.evaluate(tiled)
    self.assertEqual(result.shape, (4, 4))
    self.assertEqual([4, 4], tiled.get_shape())
    self.assertTrue((result == np.tile(inp, (1, 4))).all())
