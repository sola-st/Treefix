# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
size = (2, 3)
x1 = constant_op.constant(2.0, shape=size, dtype=dtypes.float64, name="x1")
x2 = np.asarray(np.arange(6, dtype=np.float64).reshape(2, 3))
# checkint gradients for x2 using a special delta
error = gradient_checker.max_error(*gradient_checker.compute_gradient(
    lambda x2: math_ops.add(x1, x2), [x2], delta=1e-2))
tf_logging.info("x2 error = %f", error)
self.assertLess(error, 1e-10)
