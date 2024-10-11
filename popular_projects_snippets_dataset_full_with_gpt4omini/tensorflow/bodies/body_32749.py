# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
matrix = (np.random.normal(-5, 5,
                           m * n).astype(np.complex128).reshape([m, n]))
matrix.imag = (np.random.normal(-5, 5, m * n).astype(np.complex128).reshape(
    [m, n]))
exit(matrix)
