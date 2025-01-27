# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
np.random.seed(4)  # Fix seed to avoid flakiness
with self.cached_session():
    p_shape = (4, 2)
    p_size = 8
    index_values = [1, 3]
    y_shape = [2, 2]
    params = constant_op.constant(
        np.arange(p_size).astype(np.float64), shape=p_shape, name="p")
    indices = constant_op.constant(index_values, name="i")
    y = array_ops.gather(params, indices, name="y")

    error = gradient_checker.compute_gradient_error(params, p_shape, y,
                                                    y_shape)
tf_logging.info("gather error = %f", error)
self.assertLess(error, 1e-4)
