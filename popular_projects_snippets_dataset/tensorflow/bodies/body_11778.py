# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
"""Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

    ```python
    # Make an operator acting like batch matric A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)

    X = ... # shape [..., N], batch vector

    Y = operator.matvec(X)
    Y.shape
    ==> [..., M]

    Y[..., :] = sum_j A[..., :, j] X[..., j]
    ```

    Args:
      x: `Tensor` with compatible shape and same `dtype` as `self`, or an
        iterable of `Tensor`s (for blockwise operators). `Tensor`s are treated
        a [batch] vectors, meaning for every set of leading dimensions, the last
        dimension defines a vector.
        See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      name:  A name for this `Op`.

    Returns:
      A `Tensor` with shape `[..., M]` and same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    block_dimensions = (self._block_range_dimensions() if adjoint
                        else self._block_domain_dimensions())
    if linear_operator_util.arg_is_blockwise(block_dimensions, x, -1):
        for i, block in enumerate(x):
            if not isinstance(block, linear_operator.LinearOperator):
                block = ops.convert_to_tensor_v2_with_dispatch(block)
                self._check_input_dtype(block)
                block_dimensions[i].assert_is_compatible_with(block.shape[-1])
                x[i] = block
        x_mat = [block[..., array_ops.newaxis] for block in x]
        y_mat = self.matmul(x_mat, adjoint=adjoint)
        exit([array_ops.squeeze(y, axis=-1) for y in y_mat])

    x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
    self._check_input_dtype(x)
    op_dimension = (self.range_dimension if adjoint
                    else self.domain_dimension)
    op_dimension.assert_is_compatible_with(x.shape[-1])
    x_mat = x[..., array_ops.newaxis]
    y_mat = self.matmul(x_mat, adjoint=adjoint)
    exit(array_ops.squeeze(y_mat, axis=-1))
