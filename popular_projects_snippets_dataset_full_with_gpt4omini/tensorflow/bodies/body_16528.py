# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
inputs = constant_op.constant([1.0, 2.0, 3.0, 4.0], dtype=dtypes.float32)
outputs = math_ops.maximum(inputs, 3.0)
with self.cached_session():
    error = gradient_checker.compute_gradient_error(inputs, [4], outputs, [4])
    self.assertLess(error, 1e-4)
