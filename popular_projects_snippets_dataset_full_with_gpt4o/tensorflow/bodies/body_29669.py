# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.random.rand(3, 3)
i = np.arange(3)
expected_ans = x[i, i]
self.diagPartOp(x, np.float32, expected_ans)
self.diagPartOp(x, np.float64, expected_ans)
