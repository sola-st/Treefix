# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
predictions = [[0.1, float("nan"), 0.2, 0.4], [0.1, 0.2, 0.3, float("inf")]]
target = [1, 3]
self._validateInTopK(predictions, target, 2, [False, False])
