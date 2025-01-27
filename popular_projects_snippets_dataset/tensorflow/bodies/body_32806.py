# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
l = linalg_lib.LinearOperatorLowerTriangular(
    [[1., 0.], [0.5, 0.2]], is_non_singular=True, is_positive_definite=True)
self.assertIs(l, (l @ l.H).cholesky())
