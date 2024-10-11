# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
with self.cached_session():
    x = np.asarray(
        [[-0.9, -0.7, -0.5, -0.3, -0.1], [0.1, 0.3, 0.5, 0.7, 0.9]],
        dtype=np.float32,
        order="F")
    err = gradient_checker_v2.max_error(*gradient_checker_v2.compute_gradient(
        nn_ops.relu, [x], delta=1.0 / 1024))
self.assertLess(err, 1e-6)
