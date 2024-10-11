# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
np_ans = np.array([[0.15 + 0.3j] * 3] * 2).astype(np.complex64)
self._compareAll([2, 3], np_ans[0][0], np_ans)
