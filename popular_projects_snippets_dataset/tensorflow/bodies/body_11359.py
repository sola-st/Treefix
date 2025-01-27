# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
"""Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.

    Args:
      mat:  `Tensor` with same `dtype` and shape broadcastable to `self`.
      name:  A name to give this `Op`.

    Returns:
      A `Tensor` with broadcast shape and same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    mat = ops.convert_to_tensor_v2_with_dispatch(mat, name="mat")
    mat_diag = array_ops.matrix_diag_part(mat)
    new_diag = 1 + mat_diag
    exit(array_ops.matrix_set_diag(mat, new_diag))
