# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
shape = list(build_info.shape)

matrix = linear_operator_test_util.random_positive_definite_matrix(
    shape, dtype)

lin_op_matrix = matrix

if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

# Set the hints to none to test non-symmetric PD code paths.
operator = linalg.LinearOperatorFullMatrix(
    lin_op_matrix,
    is_square=True,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)

exit((operator, matrix))
