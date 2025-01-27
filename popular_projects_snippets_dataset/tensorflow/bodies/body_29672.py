# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.random.rand(2, 2, 2, 2, 2, 2)
i = np.arange(2)[:, None, None]
j = np.arange(2)[:, None]
k = np.arange(2)
expected_ans = x[i, j, k, i, j, k]
self.diagPartOp(x, np.float32, expected_ans)
self.diagPartOp(x, np.float64, expected_ans)
