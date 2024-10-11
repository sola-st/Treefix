# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = rng.randn(2, 3, 4)
matrix_ph = array_ops.placeholder_with_default(input=matrix, shape=None)
operator = LinearOperatorMatmulSolve(matrix_ph)
expected_parameters = {
    "is_non_singular": None,
    "is_positive_definite": None,
    "is_self_adjoint": None,
    "is_square": None,
    "matrix": matrix_ph,
}
self.assertEqual(expected_parameters, operator.parameters)
