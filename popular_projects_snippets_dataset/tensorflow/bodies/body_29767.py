# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(4, 2).astype("f")
    a = array_ops.reshape(inp, [4, 1, 2, 1])
    squeezed = array_ops.squeeze(a, [1])

    err = gradient_checker.compute_gradient_error(a, [4, 1, 2, 1], squeezed,
                                                  [4, 2, 1])
self.assertLess(err, 1e-3)
