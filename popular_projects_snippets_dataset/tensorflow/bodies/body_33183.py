# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py

# Matrix is always symmetric and positive definite in this class.
del ensure_self_adjoint_and_pd

shape = list(build_info.shape)

matrix = linear_operator_test_util.random_positive_definite_matrix(
    shape, dtype, force_well_conditioned=True)

lin_op_matrix = matrix

if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

operator = linalg.LinearOperatorFullMatrix(
    lin_op_matrix,
    is_square=True,
    is_self_adjoint=True,
    is_positive_definite=True)

exit((operator, matrix))
