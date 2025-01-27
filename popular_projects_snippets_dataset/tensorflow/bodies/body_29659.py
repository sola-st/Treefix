# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
expected_ans = np.array(
    [[[[1.1, 0, 0], [0, 0, 0]], [[0, 2.2, 0], [0, 0, 0]],
      [[0, 0, 3.3], [0, 0, 0]]], [[[0, 0, 0], [4.4, 0, 0]],
                                  [[0, 0, 0], [0, 5.5, 0]], [[0, 0, 0],
                                                             [0, 0, 6.6]]]])
self.diagOp(x, np.float32, expected_ans)
self.diagOp(x, np.float64, expected_ans)
