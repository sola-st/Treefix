# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.random.rand(2, 3, 2, 3)
i = np.arange(2)[:, None]
j = np.arange(3)
expected_ans = x[i, j, i, j]
self.diagPartOp(x, np.float32, expected_ans)
self.diagPartOp(x, np.float64, expected_ans)
