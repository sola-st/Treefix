# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
data = constant_op.constant([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]],
                            dtype=dtypes.float32)
segment_ids = constant_op.constant([0, 1, 2], dtype=dtypes.int64)
self._run_gradient_check(data, segment_ids)
