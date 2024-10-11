# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
for use_gpu in False, True:
    with self.cached_session(use_gpu=use_gpu):
        a = constant_op.constant(7, shape=[], dtype=dtypes.float32)
        tiled = array_ops.tile(a, [])
        result = self.evaluate(tiled)
    self.assertEqual(result.shape, ())
    self.assertEqual([], tiled.get_shape())
    self.assertEqual(7, result)
