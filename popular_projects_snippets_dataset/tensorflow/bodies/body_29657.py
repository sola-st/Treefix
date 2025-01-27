# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
for dtype in [np.complex64, np.complex128]:
    x = np.array([1.1 + 1.1j, 2.2 + 2.2j, 3.3 + 3.3j], dtype=dtype)
    expected_ans = np.array(
        [[1.1 + 1.1j, 0 + 0j, 0 + 0j], [0 + 0j, 2.2 + 2.2j, 0 + 0j],
         [0 + 0j, 0 + 0j, 3.3 + 3.3j]],
        dtype=dtype)
    self.diagOp(x, dtype, expected_ans)
