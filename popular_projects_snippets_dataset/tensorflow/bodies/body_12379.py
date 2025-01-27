# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
np.random.seed(5)  # Fix seed to avoid flakiness
with self.cached_session():
    p_shape = (8, 2)
    p_size = 16
    index_values = [1, 3, 5, 6]
    index_values2 = [0, 2]
    y2_shape = [2, 2]

    params = constant_op.constant(
        np.arange(p_size).astype(np.float64), shape=p_shape, name="p")
    indices = constant_op.constant(index_values, name="i")
    y = array_ops.gather(params, indices, name="y")
    indices2 = constant_op.constant(index_values2, name="i2")
    y2 = array_ops.gather(y, indices2, name="y2")

    error = gradient_checker.compute_gradient_error(params, p_shape, y2,
                                                    y2_shape)
tf_logging.info("nested gather error = %f", error)
self.assertLess(error, 1e-4)
