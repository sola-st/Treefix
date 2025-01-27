# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
b = 20
m = 10
n = 15
superdiag = self._randomComplexArray((b, m - 1))
maindiag = self._randomComplexArray((b, m))
subdiag = self._randomComplexArray((b, m - 1))
rhs = self._randomComplexArray((b, m, n))
matrix = np.stack([np.diag(superdiag[i], 1) + \
                       np.diag(maindiag[i], 0) + \
                       np.diag(subdiag[i], -1) for i in range(b)])
expected_result = np.matmul(matrix, rhs)
result = linalg_impl.tridiagonal_matmul(
    constant_op.constant(matrix, dtype=dtypes.complex128),
    constant_op.constant(rhs, dtype=dtypes.complex128),
    diagonals_format='matrix')

with self.cached_session():
    result = self.evaluate(result)

self.assertAllClose(result, expected_result)
