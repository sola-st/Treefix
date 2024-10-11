# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
transp = lambda x: np.swapaxes(x, -1, -2)
for lower, adjoint in itertools.product([True, False], repeat=2):
    self._VerifyTriangularSolve(
        a if lower else transp(a), b, lower, adjoint, atol, dtype=dtype)
