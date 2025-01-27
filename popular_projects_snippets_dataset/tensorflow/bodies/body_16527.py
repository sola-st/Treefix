# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
inputs = constant_op.constant([1.0], dtype=dtypes.float32)
outputs = math_ops.reduce_max(array_ops.concat([inputs, inputs], 0))
with self.cached_session():
    error = gradient_checker.compute_gradient_error(inputs, [1], outputs, [])
    self.assertLess(error, 1e-4)
