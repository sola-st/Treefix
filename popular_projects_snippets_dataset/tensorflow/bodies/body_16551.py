# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
inputs = constant_op.constant([1.0], dtype=dtypes.float32)
data = array_ops.concat([inputs, inputs], 0)
segment_ids = constant_op.constant([0, 0], dtype=dtypes.int64)
segment_min = math_ops.segment_min(data, segment_ids)
with self.cached_session():
    error = gradient_checker.compute_gradient_error(inputs, [1], segment_min,
                                                    [1])
    self.assertLess(error, 1e-4)
