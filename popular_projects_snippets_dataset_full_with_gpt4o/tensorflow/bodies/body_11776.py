# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
"""Transform [batch] matrix `x` with left multiplication:  `x --> Ax`.

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)
    operator.shape = [..., M, N]

    X = ... # shape [..., N, R], batch matrix, R > 0.

    Y = operator.matmul(X)
    Y.shape
    ==> [..., M, R]

    Y[..., :, r] = sum_j A[..., :, j] X[j, r]
    ```

    Args:
      x: `LinearOperator`, `Tensor` with compatible shape and same `dtype` as
        `self`, or a blockwise iterable of `LinearOperator`s or `Tensor`s. See
        class docstring for definition of shape compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      adjoint_arg:  Python `bool`.  If `True`, compute `A x^H` where `x^H` is
        the hermitian transpose (transposition and complex conjugation).
      name:  A name for this `Op`.

    Returns:
      A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
        as `self`, or if `x` is blockwise, a list of `Tensor`s with shapes that
        concatenate to `[..., M, R]`.
    """
def _check_operators_agree(r, l, message):
    if (r.range_dimension is not None and
        l.domain_dimension is not None and
        r.range_dimension != l.domain_dimension):
        raise ValueError(message)

if isinstance(x, linear_operator.LinearOperator):
    left_operator = self.adjoint() if adjoint else self
    right_operator = x.adjoint() if adjoint_arg else x

    _check_operators_agree(
        right_operator, left_operator,
        "Operators are incompatible. Expected `x` to have dimension"
        " {} but got {}.".format(
            left_operator.domain_dimension, right_operator.range_dimension))

    # We can efficiently multiply BlockDiag LinearOperators if the number of
    # blocks agree.
    if isinstance(x, LinearOperatorBlockDiag):
        if len(left_operator.operators) != len(right_operator.operators):
            raise ValueError(
                "Can not efficiently multiply two `LinearOperatorBlockDiag`s "
                "together when number of blocks differ.")

        for o1, o2 in zip(left_operator.operators, right_operator.operators):
            _check_operators_agree(
                o2, o1,
                "Blocks are incompatible. Expected `x` to have dimension"
                " {} but got {}.".format(
                    o1.domain_dimension, o2.range_dimension))

    with self._name_scope(name):  # pylint: disable=not-callable
        exit(linear_operator_algebra.matmul(left_operator, right_operator))

with self._name_scope(name):  # pylint: disable=not-callable
    arg_dim = -1 if adjoint_arg else -2
    block_dimensions = (self._block_range_dimensions() if adjoint
                        else self._block_domain_dimensions())
    if linear_operator_util.arg_is_blockwise(block_dimensions, x, arg_dim):
        for i, block in enumerate(x):
            if not isinstance(block, linear_operator.LinearOperator):
                block = ops.convert_to_tensor_v2_with_dispatch(block)
                self._check_input_dtype(block)
                block_dimensions[i].assert_is_compatible_with(block.shape[arg_dim])
                x[i] = block
    else:
        x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
        self._check_input_dtype(x)
        op_dimension = (self.range_dimension if adjoint
                        else self.domain_dimension)
        op_dimension.assert_is_compatible_with(x.shape[arg_dim])
    exit(self._matmul(x, adjoint=adjoint, adjoint_arg=adjoint_arg))
