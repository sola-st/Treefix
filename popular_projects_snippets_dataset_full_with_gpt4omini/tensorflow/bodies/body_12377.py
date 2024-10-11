# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
np.random.seed(3)  # Fix seed to avoid flakiness
with self.cached_session():
    # a test case for Add operation
    size = (2, 3)
    x1 = constant_op.constant(
        2.0, shape=size, dtype=dtypes.float64, name="x1")
    x2 = constant_op.constant(
        3.0, shape=size, dtype=dtypes.float64, name="x2")
    y = math_ops.add(x1, x2, name="y")

    # checkint gradients for x2 using a special init_value and delta
    x_init_value = np.asarray(np.arange(6, dtype=np.float64).reshape(2, 3))
    error = gradient_checker.compute_gradient_error(
        x2, size, y, size, x_init_value=x_init_value, delta=1e-2)
tf_logging.info("x2 error = %f", error)
self.assertLess(error, 1e-10)
