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
    rhs = self.make_rhs(
        operator, adjoint=adjoint, with_batch=with_batch)
    # If adjoint_arg, solve A X = (rhs^H)^H = rhs.
    if adjoint_arg:
        op_solve = operator.solve(
            linalg.adjoint(rhs),
            adjoint=adjoint,
            adjoint_arg=adjoint_arg)
    else:
        op_solve = operator.solve(
            rhs, adjoint=adjoint, adjoint_arg=adjoint_arg)
    mat_solve = linear_operator_util.matrix_solve_with_broadcast(
        mat, rhs, adjoint=adjoint)
    if not use_placeholder:
        self.assertAllEqual(op_solve.shape,
                            mat_solve.shape)

    # If the operator is blockwise, test both blockwise rhs and `Tensor` rhs;
    # else test only `Tensor` rhs. In both cases, evaluate all results in a
    # single `sess.run` call to avoid re-sampling the random rhs in graph mode.
    if blockwise_arg and len(operator.operators) > 1:
        # pylint: disable=protected-access
        block_dimensions = (
            operator._block_range_dimensions() if adjoint else
            operator._block_domain_dimensions())
        block_dimensions_fn = (
            operator._block_range_dimension_tensors if adjoint else
            operator._block_domain_dimension_tensors)
        # pylint: enable=protected-access
        split_rhs = linear_operator_util.split_arg_into_blocks(
            block_dimensions,
            block_dimensions_fn,
            rhs, axis=-2)
        if adjoint_arg:
            split_rhs = [linalg.adjoint(y) for y in split_rhs]
        split_solve = operator.solve(
            split_rhs, adjoint=adjoint, adjoint_arg=adjoint_arg)
        self.assertEqual(len(split_solve), len(operator.operators))
        split_solve = linear_operator_util.broadcast_matrix_batch_dims(
            split_solve)
        fused_block_solve = array_ops.concat(split_solve, axis=-2)
        op_solve_v, mat_solve_v, fused_block_solve_v = sess.run([
            op_solve, mat_solve, fused_block_solve])

        # Check that the operator and matrix give the same solution when the rhs
        # is blockwise.
        self.assertAC(mat_solve_v, fused_block_solve_v)
    else:
        op_solve_v, mat_solve_v = sess.run([op_solve, mat_solve])

    # Check that the operator and matrix give the same solution when the rhs is
    # a `Tensor`.
    self.assertAC(op_solve_v, mat_solve_v)
