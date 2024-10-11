# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
"""Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

    The returned `Tensor` will be close to an exact solution if `A` is well
    conditioned. Otherwise closeness will vary. See class docstring for details.

    Examples:

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    # Solve R > 0 linear systems for every member of the batch.
    RHS = ... # shape [..., M, R]

    X = operator.solve(RHS)
    # X[..., :, r] is the solution to the r'th linear system
    # sum_j A[..., :, j] X[..., j, r] = RHS[..., :, r]

    operator.matmul(X)
    ==> RHS
    ```

    Args:
      rhs: `Tensor` with same `dtype` as this operator and compatible shape,
        or a list of `Tensor`s (for blockwise operators). `Tensor`s are treated
        like a [batch] matrices meaning for every set of leading dimensions, the
        last two dimensions defines a matrix.
        See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, solve the system involving the adjoint
        of this `LinearOperator`:  `A^H X = rhs`.
      adjoint_arg:  Python `bool`.  If `True`, solve `A X = rhs^H` where `rhs^H`
        is the hermitian transpose (transposition and complex conjugation).
      name:  A name scope to use for ops added by this method.

    Returns:
      `Tensor` with shape `[...,N, R]` and same `dtype` as `rhs`.

    Raises:
      NotImplementedError:  If `self.is_non_singular` or `is_square` is False.
    """
if self.is_non_singular is False:
    raise NotImplementedError(
        "Exact solve not implemented for an operator that is expected to "
        "be singular.")
if self.is_square is False:
    raise NotImplementedError(
        "Exact solve not implemented for an operator that is expected to "
        "not be square.")

def _check_operators_agree(r, l, message):
    if (r.range_dimension is not None and
        l.domain_dimension is not None and
        r.range_dimension != l.domain_dimension):
        raise ValueError(message)

if isinstance(rhs, linear_operator.LinearOperator):
    left_operator = self.adjoint() if adjoint else self
    right_operator = rhs.adjoint() if adjoint_arg else rhs

    _check_operators_agree(
        right_operator, left_operator,
        "Operators are incompatible. Expected `x` to have dimension"
        " {} but got {}.".format(
            left_operator.domain_dimension, right_operator.range_dimension))

    # We can efficiently solve BlockDiag LinearOperators if the number of
    # blocks agree.
    if isinstance(right_operator, LinearOperatorBlockDiag):
        if len(left_operator.operators) != len(right_operator.operators):
            raise ValueError(
                "Can not efficiently solve `LinearOperatorBlockDiag` when "
                "number of blocks differ.")

        for o1, o2 in zip(left_operator.operators, right_operator.operators):
            _check_operators_agree(
                o2, o1,
                "Blocks are incompatible. Expected `x` to have dimension"
                " {} but got {}.".format(
                    o1.domain_dimension, o2.range_dimension))

    with self._name_scope(name):  # pylint: disable=not-callable
        exit(linear_operator_algebra.solve(left_operator, right_operator))

with self._name_scope(name):  # pylint: disable=not-callable
    block_dimensions = (self._block_domain_dimensions() if adjoint
                        else self._block_range_dimensions())
    arg_dim = -1 if adjoint_arg else -2
    blockwise_arg = linear_operator_util.arg_is_blockwise(
        block_dimensions, rhs, arg_dim)

    if blockwise_arg:
        split_rhs = rhs
        for i, block in enumerate(split_rhs):
            if not isinstance(block, linear_operator.LinearOperator):
                block = ops.convert_to_tensor_v2_with_dispatch(block)
                self._check_input_dtype(block)
                block_dimensions[i].assert_is_compatible_with(block.shape[arg_dim])
                split_rhs[i] = block
    else:
        rhs = ops.convert_to_tensor_v2_with_dispatch(rhs, name="rhs")
        self._check_input_dtype(rhs)
        op_dimension = (self.domain_dimension if adjoint
                        else self.range_dimension)
        op_dimension.assert_is_compatible_with(rhs.shape[arg_dim])
        split_dim = -1 if adjoint_arg else -2
        # Split input by rows normally, and otherwise columns.
        split_rhs = linear_operator_util.split_arg_into_blocks(
            self._block_domain_dimensions(),
            self._block_domain_dimension_tensors,
            rhs, axis=split_dim)

    solution_list = []
    for index, operator in enumerate(self.operators):
        solution_list += [operator.solve(
            split_rhs[index], adjoint=adjoint, adjoint_arg=adjoint_arg)]

    if blockwise_arg:
        exit(solution_list)

    solution_list = linear_operator_util.broadcast_matrix_batch_dims(
        solution_list)
    exit(array_ops.concat(solution_list, axis=-2))
