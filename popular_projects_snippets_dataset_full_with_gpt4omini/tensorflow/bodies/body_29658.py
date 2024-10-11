# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.array([[1, 2, 3], [4, 5, 6]])
expected_ans = np.array([[[[1, 0, 0], [0, 0, 0]], [[0, 2, 0], [0, 0, 0]],
                          [[0, 0, 3], [0, 0, 0]]],
                         [[[0, 0, 0], [4, 0, 0]], [[0, 0, 0], [0, 5, 0]],
                          [[0, 0, 0], [0, 0, 6]]]])
self.diagOp(x, np.int32, expected_ans)
self.diagOp(x, np.int64, expected_ans)
