# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
"""Solve (exact or approx) `R` (batch) systems of equations: `A X = rhs`.

    The returned `Tensor` will be close to an exact solution if `A` is well
    conditioned. Otherwise closeness will vary. See class docstring for details.

    Given the blockwise `n + 1`-by-`n + 1` linear operator:

    op = [[A_00     0  ...     0  ...    0],
          [A_10  A_11  ...     0  ...    0],
          ...
          [A_k0  A_k1  ...  A_kk  ...    0],
          ...
          [A_n0  A_n1  ...  A_nk  ... A_nn]]

    we find `x = op.solve(y)` by observing that

    `y_k = A_k0.matmul(x_0) + A_k1.matmul(x_1) + ... + A_kk.matmul(x_k)`

    and therefore

    `x_k = A_kk.solve(y_k -
                      A_k0.matmul(x_0) - ... - A_k(k-1).matmul(x_(k-1)))`

    where `x_k` and `y_k` are the `k`th blocks obtained by decomposing `x`
    and `y` along their appropriate axes.

    We first solve `x_0 = A_00.solve(y_0)`. Proceeding inductively, we solve
    for `x_k`, `k = 1..n`, given `x_0..x_(k-1)`.

    The adjoint case is solved similarly, beginning with
    `x_n = A_nn.solve(y_n, adjoint=True)` and proceeding backwards.

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
        or a list of `Tensor`s. `Tensor`s are treated like a [batch] matrices
        meaning for every set of leading dimensions, the last two dimensions
        defines a matrix.
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
if isinstance(rhs, linear_operator.LinearOperator):
    left_operator = self.adjoint() if adjoint else self
    right_operator = rhs.adjoint() if adjoint_arg else rhs

    if (right_operator.range_dimension is not None and
        left_operator.domain_dimension is not None and
        right_operator.range_dimension != left_operator.domain_dimension):
        raise ValueError(
            "Operators are incompatible. Expected `rhs` to have dimension"
            " {} but got {}.".format(
                left_operator.domain_dimension, right_operator.range_dimension))
    with self._name_scope(name):  # pylint: disable=not-callable
        exit(linear_operator_algebra.solve(left_operator, right_operator))

with self._name_scope(name):  # pylint: disable=not-callable
    block_dimensions = (self._block_domain_dimensions() if adjoint
                        else self._block_range_dimensions())
    arg_dim = -1 if adjoint_arg else -2
    blockwise_arg = linear_operator_util.arg_is_blockwise(
        block_dimensions, rhs, arg_dim)
    if blockwise_arg:
        for i, block in enumerate(rhs):
            if not isinstance(block, linear_operator.LinearOperator):
                block = ops.convert_to_tensor_v2_with_dispatch(block)
                self._check_input_dtype(block)
                block_dimensions[i].assert_is_compatible_with(block.shape[arg_dim])
                rhs[i] = block
        if adjoint_arg:
            split_rhs = [linalg.adjoint(y) for y in rhs]
        else:
            split_rhs = rhs

    else:
        rhs = ops.convert_to_tensor_v2_with_dispatch(rhs, name="rhs")
        self._check_input_dtype(rhs)
        op_dimension = (self.domain_dimension if adjoint
                        else self.range_dimension)
        op_dimension.assert_is_compatible_with(rhs.shape[arg_dim])

        rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
        split_rhs = linear_operator_util.split_arg_into_blocks(
            self._block_domain_dimensions(),
            self._block_domain_dimension_tensors,
            rhs, axis=-2)

    solution_list = []
    if adjoint:
        # For an adjoint blockwise lower-triangular linear operator, the system
        # must be solved bottom to top. Iterate backwards over rows of the
        # adjoint (i.e. columns of the non-adjoint operator).
        for index in reversed(range(len(self.operators))):
            y = split_rhs[index]
            # Iterate top to bottom over the operators in the off-diagonal portion
            # of the column-partition (i.e. row-partition of the adjoint), apply
            # the operator to the respective block of the solution found in
            # previous iterations, and subtract the result from the `rhs` block.
            # For example,let `A`, `B`, and `D` be the linear operators in the top
            # row-partition of the adjoint of
            # `LinearOperatorBlockLowerTriangular([[A], [B, C], [D, E, F]])`,
            # and `x_1` and `x_2` be blocks of the solution found in previous
            # iterations of the outer loop. The following loop (when `index == 0`)
            # expresses
            # `Ax_0 + Bx_1 + Dx_2 = y_0` as `Ax_0 = y_0*`, where
            # `y_0* = y_0 - Bx_1 - Dx_2`.
            for j in reversed(range(index + 1, len(self.operators))):
                y = y - self.operators[j][index].matmul(
                    solution_list[len(self.operators) - 1 - j],
                    adjoint=adjoint)
            # Continuing the example above, solve `Ax_0 = y_0*` for `x_0`.
            solution_list.append(
                self._diagonal_operators[index].solve(y, adjoint=adjoint))
        solution_list.reverse()
    else:
        # Iterate top to bottom over the row-partitions.
        for row, y in zip(self.operators, split_rhs):
            # Iterate left to right over the operators in the off-diagonal portion
            # of the row-partition, apply the operator to the block of the
            # solution found in previous iterations, and subtract the result from
            # the `rhs` block. For example, let `D`, `E`, and `F` be the linear
            # operators in the bottom row-partition of
            # `LinearOperatorBlockLowerTriangular([[A], [B, C], [D, E, F]])` and
            # `x_0` and `x_1` be blocks of the solution found in previous
            # iterations of the outer loop. The following loop
            # (when `index == 2`), expresses
            # `Dx_0 + Ex_1 + Fx_2 = y_2` as `Fx_2 = y_2*`, where
            # `y_2* = y_2 - D_x0 - Ex_1`.
            for i, operator in enumerate(row[:-1]):
                y = y - operator.matmul(solution_list[i], adjoint=adjoint)
            # Continuing the example above, solve `Fx_2 = y_2*` for `x_2`.
            solution_list.append(row[-1].solve(y, adjoint=adjoint))

    if blockwise_arg:
        exit(solution_list)

    solution_list = linear_operator_util.broadcast_matrix_batch_dims(
        solution_list)
    exit(array_ops.concat(solution_list, axis=-2))
