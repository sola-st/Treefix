# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
for n in 2, 5:
    matrix = self._generateMatrix(n, n)
    for nrhs in 1, n:
        rhs = self._generateMatrix(n, nrhs)
        for batch_dims in [[2], [2, 2], [7, 4]]:
            self._verifySolve(matrix, rhs, batch_dims=batch_dims)
