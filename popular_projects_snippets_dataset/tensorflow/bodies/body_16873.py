# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
size = (2, 3)
x1 = constant_op.constant(2.0, shape=size, name="x1")
x2 = constant_op.constant(3.0, shape=size, name="x2")
error = gradient_checker.max_error(*gradient_checker.compute_gradient(
    lambda x1: math_ops.add(x1, x2), [x1]))
tf_logging.info("x1 error = %f", error)
self.assertLess(error, 1e-4)
