# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
# Kronecker products constructed below will be from symmetric
# positive-definite matrices.
del ensure_self_adjoint_and_pd
shape = list(build_info.shape)
expected_factors = build_info.__dict__["factors"]
matrices = [
    linear_operator_test_util.random_positive_definite_matrix(
        block_shape, dtype, force_well_conditioned=True)
    for block_shape in expected_factors
]

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(m, shape=None) for m in matrices]

operator = kronecker.LinearOperatorKronecker(
    [linalg.LinearOperatorFullMatrix(
        l,
        is_square=True,
        is_self_adjoint=True,
        is_positive_definite=True)
     for l in lin_op_matrices])

matrices = linear_operator_util.broadcast_matrix_batch_dims(matrices)

kronecker_dense = _kronecker_dense(matrices)

if not use_placeholder:
    kronecker_dense.set_shape(shape)

exit((operator, kronecker_dense))
