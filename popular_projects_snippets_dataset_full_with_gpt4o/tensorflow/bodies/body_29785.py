# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(4, 2).astype("f")
    a = constant_op.constant(
        [float(x) for x in inp.flatten()], shape=[4, 2], dtype=dtypes.float32)
    tiled = array_ops.tile(a, [1, 2])
    err = gradient_checker.compute_gradient_error(a, [4, 2], tiled, [4, 4])
self.assertLess(err, 1e-3)
