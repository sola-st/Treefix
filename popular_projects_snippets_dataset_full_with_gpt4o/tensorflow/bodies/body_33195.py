# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
shape = list(build_info.shape)

if ensure_self_adjoint_and_pd:
    matrix = linear_operator_test_util.random_positive_definite_matrix(
        shape, dtype, force_well_conditioned=True)
else:
    matrix = linear_operator_test_util.random_tril_matrix(
        shape, dtype, force_well_conditioned=True, remove_upper=True)

lin_op_matrix = matrix

if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

if ensure_self_adjoint_and_pd:
    operator = LinearOperatorAdjoint(
        linalg.LinearOperatorFullMatrix(
            lin_op_matrix, is_positive_definite=True, is_self_adjoint=True))
else:
    operator = LinearOperatorAdjoint(
        linalg.LinearOperatorLowerTriangular(lin_op_matrix))

exit((operator, linalg.adjoint(matrix)))
