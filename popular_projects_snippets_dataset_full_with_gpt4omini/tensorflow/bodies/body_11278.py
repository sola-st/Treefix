# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
# If batch dimensions are omitted, but there are
# no batch dimensions for the linear operator, then
# skip the test case. This is already checked with
# with_batch=True.
if not with_batch and len(shapes_info.shape) <= 2:
    exit()
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    x = self.make_x(
        operator, adjoint=adjoint, with_batch=with_batch)
    # If adjoint_arg, compute A X^H^H = A X.
    if adjoint_arg:
        op_matmul = operator.matmul(
            linalg.adjoint(x),
            adjoint=adjoint,
            adjoint_arg=adjoint_arg)
    else:
        op_matmul = operator.matmul(x, adjoint=adjoint)
    mat_matmul = math_ops.matmul(mat, x, adjoint_a=adjoint)
    if not use_placeholder:
        self.assertAllEqual(op_matmul.shape,
                            mat_matmul.shape)

    # If the operator is blockwise, test both blockwise `x` and `Tensor` `x`;
    # else test only `Tensor` `x`. In both cases, evaluate all results in a
    # single `sess.run` call to avoid re-sampling the random `x` in graph mode.
    if blockwise_arg and len(operator.operators) > 1:
        # pylint: disable=protected-access
        block_dimensions = (
            operator._block_range_dimensions() if adjoint else
            operator._block_domain_dimensions())
        block_dimensions_fn = (
            operator._block_range_dimension_tensors if adjoint else
            operator._block_domain_dimension_tensors)
        # pylint: enable=protected-access
        split_x = linear_operator_util.split_arg_into_blocks(
            block_dimensions,
            block_dimensions_fn,
            x, axis=-2)
        if adjoint_arg:
            split_x = [linalg.adjoint(y) for y in split_x]
        split_matmul = operator.matmul(
            split_x, adjoint=adjoint, adjoint_arg=adjoint_arg)

        self.assertEqual(len(split_matmul), len(operator.operators))
        split_matmul = linear_operator_util.broadcast_matrix_batch_dims(
            split_matmul)
        fused_block_matmul = array_ops.concat(split_matmul, axis=-2)
        op_matmul_v, mat_matmul_v, fused_block_matmul_v = sess.run([
            op_matmul, mat_matmul, fused_block_matmul])

        # Check that the operator applied to blockwise input gives the same result
        # as matrix multiplication.
        self.assertAC(fused_block_matmul_v, mat_matmul_v)
    else:
        op_matmul_v, mat_matmul_v = sess.run([op_matmul, mat_matmul])

    # Check that the operator applied to a `Tensor` gives the same result as
    # matrix multiplication.
    self.assertAC(op_matmul_v, mat_matmul_v)
