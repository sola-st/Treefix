# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
del ensure_self_adjoint_and_pd
shape = list(shape_info.shape)
expected_blocks = (
    shape_info.__dict__["blocks"] if "blocks" in shape_info.__dict__
    else [shape])
matrices = [
    linear_operator_test_util.random_normal(block_shape, dtype=dtype)
    for block_shape in expected_blocks
]

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

blocks = []
for l in lin_op_matrices:
    blocks.append(
        linalg.LinearOperatorFullMatrix(
            l,
            is_square=False,
            is_self_adjoint=False,
            is_positive_definite=False))
operator = block_diag.LinearOperatorBlockDiag(blocks)

# Broadcast the shapes.
expected_shape = list(shape_info.shape)

matrices = linear_operator_util.broadcast_matrix_batch_dims(matrices)

block_diag_dense = _block_diag_dense(expected_shape, matrices)

if not use_placeholder:
    block_diag_dense.set_shape(expected_shape)

exit((operator, block_diag_dense))
