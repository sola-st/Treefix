# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
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
      x: `LinearOperator` or `Tensor` with compatible shape and same `dtype` as
        `self`. See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      adjoint_arg:  Python `bool`.  If `True`, compute `A x^H` where `x^H` is
        the hermitian transpose (transposition and complex conjugation).
      name:  A name for this `Op`.

    Returns:
      A `LinearOperator` or `Tensor` with shape `[..., M, R]` and same `dtype`
        as `self`.
    """
if isinstance(x, LinearOperator):
    left_operator = self.adjoint() if adjoint else self
    right_operator = x.adjoint() if adjoint_arg else x

    if (right_operator.range_dimension is not None and
        left_operator.domain_dimension is not None and
        right_operator.range_dimension != left_operator.domain_dimension):
        raise ValueError(
            "Operators are incompatible. Expected `x` to have dimension"
            " {} but got {}.".format(
                left_operator.domain_dimension, right_operator.range_dimension))
    with self._name_scope(name):  # pylint: disable=not-callable
        exit(linear_operator_algebra.matmul(left_operator, right_operator))

with self._name_scope(name):  # pylint: disable=not-callable
    x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
    self._check_input_dtype(x)

    self_dim = -2 if adjoint else -1
    arg_dim = -1 if adjoint_arg else -2
    tensor_shape.dimension_at_index(
        self.shape, self_dim).assert_is_compatible_with(
            x.shape[arg_dim])

    exit(self._matmul(x, adjoint=adjoint, adjoint_arg=adjoint_arg))
