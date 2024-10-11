# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = [[np.NaN, np.NaN], [np.NaN, np.NaN]]
self._validateTopK(inputs, 1, [[np.NaN], [np.NaN]], [[0], [0]])
