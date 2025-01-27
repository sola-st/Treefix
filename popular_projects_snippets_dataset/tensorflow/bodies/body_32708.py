# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
shape = list(shape_info.shape)
expected_blocks = (
    shape_info.__dict__["blocks"] if "blocks" in shape_info.__dict__
    else [shape])
matrices = [
    linear_operator_test_util.random_positive_definite_matrix(
        block_shape, dtype, force_well_conditioned=True)
    for block_shape in expected_blocks
]

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

operator = block_diag.LinearOperatorBlockDiag(
    [linalg.LinearOperatorFullMatrix(
        l,
        is_square=True,
        is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
        is_positive_definite=True if ensure_self_adjoint_and_pd else None)
     for l in lin_op_matrices])

# Should be auto-set.
self.assertTrue(operator.is_square)

# Broadcast the shapes.
expected_shape = list(shape_info.shape)

matrices = linear_operator_util.broadcast_matrix_batch_dims(matrices)

block_diag_dense = _block_diag_dense(expected_shape, matrices)

if not use_placeholder:
    block_diag_dense.set_shape(
        expected_shape[:-2] + [expected_shape[-1], expected_shape[-1]])

exit((operator, block_diag_dense))
