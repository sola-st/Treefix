# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
shape = list(build_info.shape)
# Upper triangle will be nonzero, but ignored.
# Use a diagonal that ensures this matrix is well conditioned.
tril = linear_operator_test_util.random_tril_matrix(
    shape, dtype=dtype, force_well_conditioned=True, remove_upper=False)
if ensure_self_adjoint_and_pd:
    # Get the diagonal and make the matrix out of it.
    tril = array_ops.matrix_diag_part(tril)
    tril = math_ops.abs(tril) + 1e-1
    tril = array_ops.matrix_diag(tril)

lin_op_tril = tril

if use_placeholder:
    lin_op_tril = array_ops.placeholder_with_default(lin_op_tril, shape=None)

operator = linalg.LinearOperatorLowerTriangular(
    lin_op_tril,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)

matrix = array_ops.matrix_band_part(tril, -1, 0)

exit((operator, matrix))
