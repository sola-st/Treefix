# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
for dtype in [dtypes.complex64, dtypes.complex128]:
    self._testAllFormats([1j, 1j], [1, -1, 0], [1j, 1j],
                         np.array([[1, 1j], [1, 1j], [1, 1j]]),
                         [[1 + 1j, -1 + 1j], [-1 + 2j, -2 - 1j], [1j, -1]],
                         dtype=dtype)
