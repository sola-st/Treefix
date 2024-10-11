# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py

expected_blocks = (
    shape_info.__dict__["blocks"] if "blocks" in shape_info.__dict__
    else [[list(shape_info.shape)]])

matrices = []
for i, row_shapes in enumerate(expected_blocks):
    row = []
    for j, block_shape in enumerate(row_shapes):
        if i == j:  # operator is on the diagonal
            row.append(
                linear_operator_test_util.random_positive_definite_matrix(
                    block_shape, dtype, force_well_conditioned=True))
        else:
            row.append(
                linear_operator_test_util.random_normal(block_shape, dtype=dtype))
    matrices.append(row)

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [[
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in row] for row in matrices]

operator = block_lower_triangular.LinearOperatorBlockLowerTriangular(
    [[linalg.LinearOperatorFullMatrix(  # pylint:disable=g-complex-comprehension
        l,
        is_square=True,
        is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
        is_positive_definite=True if ensure_self_adjoint_and_pd else None)
      for l in row] for row in lin_op_matrices])

# Should be auto-set.
self.assertTrue(operator.is_square)

# Broadcast the shapes.
expected_shape = list(shape_info.shape)
broadcasted_matrices = linear_operator_util.broadcast_matrix_batch_dims(
    [op for row in matrices for op in row])  # pylint: disable=g-complex-comprehension
matrices = [broadcasted_matrices[i * (i + 1) // 2:(i + 1) * (i + 2) // 2]
            for i in range(len(matrices))]

block_lower_triangular_dense = _block_lower_triangular_dense(
    expected_shape, matrices)

if not use_placeholder:
    block_lower_triangular_dense.set_shape(expected_shape)

exit((operator, block_lower_triangular_dense))
