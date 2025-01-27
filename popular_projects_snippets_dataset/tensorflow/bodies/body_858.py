# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_solve_op_test.py
matrix = np.random.normal(-5.0, 5.0, batch_dims + [n, n])
rhs = np.random.normal(-5.0, 5.0, rhs_batch_dims + [n, nrhs])
self._verifySolve(matrix, rhs, adjoint=adjoint)
