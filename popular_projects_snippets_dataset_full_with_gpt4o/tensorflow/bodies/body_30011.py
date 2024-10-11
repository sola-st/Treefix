# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
np_ans = np.array([[-42] * 3] * 2).astype(np.int64)
self._compareAll([2, 3], np_ans[0][0], np_ans)
