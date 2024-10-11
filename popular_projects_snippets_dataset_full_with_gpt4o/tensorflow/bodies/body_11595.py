# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Add matrix represented by this operator to `x`.  Equivalent to `A + x`.

    Args:
      x:  `Tensor` with same `dtype` and shape broadcastable to `self.shape`.
      name:  A name to give this `Op`.

    Returns:
      A `Tensor` with broadcast shape and same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    x = ops.convert_to_tensor_v2_with_dispatch(x, name="x")
    self._check_input_dtype(x)
    exit(self._add_to_tensor(x))
