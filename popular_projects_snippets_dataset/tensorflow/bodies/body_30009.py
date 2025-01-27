# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
np_ans = np.array([[3.1415] * 3] * 2).astype(np.float64)
self._compareAll([2, 3], np_ans[0][0], np_ans)
