# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
predictions = [[0.1, 0.3, 0.2, 0.4], [0.1, 0.2, 0.3, 0.4]]
target = [2, 2]
self._validateInTopK(predictions, target, 2, [False, True])
