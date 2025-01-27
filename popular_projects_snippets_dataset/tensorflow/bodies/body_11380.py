# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
"""Add matrix represented by this operator to `mat`.  Equiv to `I + mat`.

    Args:
      mat:  `Tensor` with same `dtype` and shape broadcastable to `self`.
      name:  A name to give this `Op`.

    Returns:
      A `Tensor` with broadcast shape and same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    # Shape [B1,...,Bb, 1]
    multiplier_vector = array_ops.expand_dims(self.multiplier, -1)

    # Shape [C1,...,Cc, M, M]
    mat = ops.convert_to_tensor_v2_with_dispatch(mat, name="mat")

    # Shape [C1,...,Cc, M]
    mat_diag = array_ops.matrix_diag_part(mat)

    # multiplier_vector broadcasts here.
    new_diag = multiplier_vector + mat_diag

    exit(array_ops.matrix_set_diag(mat, new_diag))
