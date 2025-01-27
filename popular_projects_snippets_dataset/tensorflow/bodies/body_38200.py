# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
inputs = constant_op.constant([1.0, 2.0, 3.0, 4.0], dtype=dtypes.float32)
outputs_1 = clip_ops.clip_by_value(inputs, 0.5, 3.5)
min_val = constant_op.constant([0.5, 0.5, 0.5, 0.5], dtype=dtypes.float32)
max_val = constant_op.constant([3.5, 3.5, 3.5, 3.5], dtype=dtypes.float32)
outputs_2 = clip_ops.clip_by_value(inputs, min_val, max_val)
with self.cached_session():
    error_1 = gradient_checker.compute_gradient_error(inputs, [4], outputs_1,
                                                      [4])
    self.assertLess(error_1, 1e-4)

    error_2 = gradient_checker.compute_gradient_error(inputs, [4], outputs_2,
                                                      [4])
    self.assertLess(error_2, 1e-4)
