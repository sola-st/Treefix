# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
# Class 2 and 3 tie for 2nd, so both are considered in top 2.
predictions = [[0.1, 0.3, 0.2, 0.2], [0.1, 0.3, 0.2, 0.2]]
target = [2, 3]
self._validateInTopK(predictions, target, 2, [True, True])
