# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
exit(set(super(MatrixTriangularSolveOpTest,
                 self).float_types).intersection(
                     (np.float64, np.float32, np.complex64, np.complex128)))
