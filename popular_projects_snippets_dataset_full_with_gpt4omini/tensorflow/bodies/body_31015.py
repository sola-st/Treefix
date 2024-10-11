# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
with self.cached_session():
    x = np.asarray(
        [[-0.9, -0.7, -0.5, -0.3, -0.1], [6.1, 6.3, 6.5, 6.7, 6.9]],
        dtype=np.float64,
        order="F")
    err = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(nn_ops.relu6, [x]))
self.assertLess(err, 1e-10)
