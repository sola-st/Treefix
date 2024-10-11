# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.array([])
expected_ans = np.empty([0, 0])
self.diagOp(x, np.int32, expected_ans)
