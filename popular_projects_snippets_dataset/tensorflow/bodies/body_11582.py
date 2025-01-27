# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
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
      rhs: `Tensor` with same `dtype` as this operator and compatible shape.
        `rhs` is treated like a [batch] matrix meaning for every set of leading
        dimensions, the last two dimensions defines a matrix.
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
if isinstance(rhs, LinearOperator):
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
    rhs = ops.convert_to_tensor_v2_with_dispatch(rhs, name="rhs")
    self._check_input_dtype(rhs)

    self_dim = -1 if adjoint else -2
    arg_dim = -1 if adjoint_arg else -2
    tensor_shape.dimension_at_index(
        self.shape, self_dim).assert_is_compatible_with(
            rhs.shape[arg_dim])

    exit(self._solve(rhs, adjoint=adjoint, adjoint_arg=adjoint_arg))
