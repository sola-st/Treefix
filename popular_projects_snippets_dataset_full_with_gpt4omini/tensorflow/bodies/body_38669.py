# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
predictions = [[0.1, 0.3, 0.2, 0.2], [0.1, 0.3, 0.2, 0.2]]
target = [2, 4]  # must return False for invalid target
self._validateInTopK(predictions, target, 2, [True, False])
