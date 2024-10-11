# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
"""Solve single equation with best effort: `A X = rhs`.

    The returned `Tensor` will be close to an exact solution if `A` is well
    conditioned. Otherwise closeness will vary. See class docstring for details.

    Examples:

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    # Solve one linear system for every member of the batch.
    RHS = ... # shape [..., M]

    X = operator.solvevec(RHS)
    # X is the solution to the linear system
    # sum_j A[..., :, j] X[..., j] = RHS[..., :]

    operator.matvec(X)
    ==> RHS
    ```

    Args:
      rhs: `Tensor` with same `dtype` as this operator, or list of `Tensor`s
        (for blockwise operators). `Tensor`s are treated as [batch] vectors,
        meaning for every set of leading dimensions, the last dimension defines
        a vector.  See class docstring for definition of compatibility regarding
        batch dimensions.
      adjoint: Python `bool`.  If `True`, solve the system involving the adjoint
        of this `LinearOperator`:  `A^H X = rhs`.
      name:  A name scope to use for ops added by this method.

    Returns:
      `Tensor` with shape `[...,N]` and same `dtype` as `rhs`.

    Raises:
      NotImplementedError:  If `self.is_non_singular` or `is_square` is False.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    block_dimensions = (self._block_domain_dimensions() if adjoint
                        else self._block_range_dimensions())
    if linear_operator_util.arg_is_blockwise(block_dimensions, rhs, -1):
        for i, block in enumerate(rhs):
            if not isinstance(block, linear_operator.LinearOperator):
                block = ops.convert_to_tensor_v2_with_dispatch(block)
                self._check_input_dtype(block)
                block_dimensions[i].assert_is_compatible_with(block.shape[-1])
                rhs[i] = block
        rhs_mat = [array_ops.expand_dims(block, axis=-1) for block in rhs]
        solution_mat = self.solve(rhs_mat, adjoint=adjoint)
        exit([array_ops.squeeze(x, axis=-1) for x in solution_mat])

    rhs = ops.convert_to_tensor_v2_with_dispatch(rhs, name="rhs")
    self._check_input_dtype(rhs)
    op_dimension = (self.domain_dimension if adjoint
                    else self.range_dimension)
    op_dimension.assert_is_compatible_with(rhs.shape[-1])
    rhs_mat = array_ops.expand_dims(rhs, axis=-1)
    solution_mat = self.solve(rhs_mat, adjoint=adjoint)
    exit(array_ops.squeeze(solution_mat, axis=-1))
