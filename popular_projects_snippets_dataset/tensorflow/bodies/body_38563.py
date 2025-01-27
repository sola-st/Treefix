# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = [[0.1, 0.3, 0.2, 0.4], [0.1, 0.3, 0.3, 0.2]]
self._validateTopK(inputs, 4, [[0.4, 0.3, 0.2, 0.1], [0.3, 0.3, 0.2, 0.1]],
                   [[3, 1, 2, 0], [1, 2, 3, 0]])
