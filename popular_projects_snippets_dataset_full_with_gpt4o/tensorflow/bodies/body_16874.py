# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
x1 = constant_op.constant(2.0, dtype="bfloat16")
x2 = constant_op.constant(3.0, dtype="bfloat16")
# bfloat16 is very imprecise, so we use very large delta and error bar here.
error = gradient_checker.max_error(*gradient_checker.compute_gradient(
    lambda x1: math_ops.add(x1, x2), [x1], delta=0.1))
tf_logging.info("x1 error = %f", error)
self.assertLess(error, 0.07)
