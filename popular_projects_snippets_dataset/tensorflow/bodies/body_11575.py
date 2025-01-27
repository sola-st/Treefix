# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Transform [batch] vector `x` with left multiplication:  `x --> Ax`.

    ```python
    # Make an operator acting like batch matrix A.  Assume A.shape = [..., M, N]
    operator = LinearOperator(...)

    X = ... # shape [..., N], batch vector

    Y = operator.matvec(X)
    Y.shape
    ==> [..., M]

    Y[..., :] = sum_j A[..., :, j] X[..., j]
    ```

    Args:
      x: `Tensor` with compatible shape and same `dtype` as `self`.
        `x` is treated as a [batch] vector meaning for every set of leading
        dimensions, the last dimension defines a vector.
        See class docstring for definition of compatibility.
      adjoint: Python `bool`.  If `True`, left multiply by the adjoint: `A^H x`.
      name:  A name for this `Op`.

    Returns:
      A `Tensor` with shape `[..., M]` and same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
    self._check_input_dtype(x)
    self_dim = -2 if adjoint else -1
    tensor_shape.dimension_at_index(
        self.shape, self_dim).assert_is_compatible_with(x.shape[-1])
    exit(self._matvec(x, adjoint=adjoint))
