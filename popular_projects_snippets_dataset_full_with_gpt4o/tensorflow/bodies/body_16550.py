# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
data = constant_op.constant([1.0, 2.0, 3.0], dtype=dtypes.float32)
segment_ids = constant_op.constant([0, 0, 1], dtype=dtypes.int64)
segment_max = math_ops.segment_max(data, segment_ids)
with self.cached_session():
    error = gradient_checker.compute_gradient_error(data, [3], segment_max,
                                                    [2])
    self.assertLess(error, 1e-4)
