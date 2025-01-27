# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.random.rand(2, 2, 2, 3, 2, 2, 2, 3)
i = np.arange(2)[:, None, None, None]
j = np.arange(2)[:, None, None]
k = np.arange(2)[:, None]
l = np.arange(3)
expected_ans = x[i, j, k, l, i, j, k, l]
self.diagPartOp(x, np.complex64, expected_ans)
self.diagPartOp(x, np.complex128, expected_ans)
