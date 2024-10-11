# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = constant_op.constant(
        np.random.rand(4, 2).astype("f"), dtype=dtypes.float32)
    squeezed = array_ops.expand_dims(inp, 1)

    err = gradient_checker.compute_gradient_error(inp, [4, 2], squeezed,
                                                  [4, 1, 2])
self.assertLess(err, 1e-3)
