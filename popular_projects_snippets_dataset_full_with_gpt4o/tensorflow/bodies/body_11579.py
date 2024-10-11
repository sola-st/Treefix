# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Log absolute value of determinant for every batch member.

    Args:
      name:  A name for this `Op`.

    Returns:
      `Tensor` with shape `self.batch_shape` and same `dtype` as `self`.

    Raises:
      NotImplementedError:  If `self.is_square` is `False`.
    """
if self.is_square is False:
    raise NotImplementedError(
        "Determinant not implemented for an operator that is expected to "
        "not be square.")
with self._name_scope(name):  # pylint: disable=not-callable
    exit(self._log_abs_determinant())
