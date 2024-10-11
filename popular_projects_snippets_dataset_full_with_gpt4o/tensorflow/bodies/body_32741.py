# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
self._gradientTest(
    np.array([[[1 + 1j, 2j, 0], [1 + 2j, 2j, 3 + 0j], [0, 1j, 2 + 0j]]]),
    np.array([[[1j, 2 + 0j], [3 + 1j, 4j], [5j, 6 + 3j]]]),
    dtype=dtypes.complex128)
