# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
b = 5
m = 10
n = 15
diags = self._randomComplexArray((b, 3, m))
rhs = self._randomComplexArray((b, m, n))
self._gradientTest(diags, rhs, dtype=dtypes.complex128)
