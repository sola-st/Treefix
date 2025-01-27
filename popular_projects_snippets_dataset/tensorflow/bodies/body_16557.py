# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
data = constant_op.constant([[0, 2, 3, 4], [0, 0, 2, 0], [5, 0, 7, 0]],
                            dtype=dtypes.float32)
segment_ids = constant_op.constant([0, 0, 1], dtype=dtypes.int64)
self._run_gradient_check(data, segment_ids)
