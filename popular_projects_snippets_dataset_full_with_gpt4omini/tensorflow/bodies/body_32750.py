# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
for n in 1, 2, 4, 9:
    matrix = self._generateMatrix(n, n)
    for nrhs in 1, 2, n:
        rhs = self._generateMatrix(n, nrhs)
        self._verifySolve(matrix, rhs)
