# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
np.random.seed(2)  # Fix seed to avoid flakiness
with self.session():
    # a test case for Add operation
    size = (2, 3)
    x1 = constant_op.constant(2.0, shape=size, name="x1")
    x2 = constant_op.constant(3.0, shape=size, name="x2")
    y = math_ops.add(x1, x2, name="y")

    # checking gradients for x1
    error = gradient_checker.compute_gradient_error(x1, size, y, size)
tf_logging.info("x1 error = %f", error)
self.assertLess(error, 1e-4)
