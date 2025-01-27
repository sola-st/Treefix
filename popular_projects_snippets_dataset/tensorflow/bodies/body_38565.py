# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = [3, 6, 15, 18, 6, 12, 1, 17, 3, 0, 4, 19, 1, 6]
self._validateTopK(inputs, 3, [19, 18, 17], [11, 3, 7])
