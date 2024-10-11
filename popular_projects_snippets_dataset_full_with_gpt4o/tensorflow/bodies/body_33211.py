# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
b1 = b + np.zeros(a.shape[:-2] + (1, 1), dtype=b.dtype)
exit((a, b1))
