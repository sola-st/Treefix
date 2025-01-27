# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Trace of the linear operator, equal to sum of `self.diag_part()`.

    If the operator is square, this is also the sum of the eigenvalues.

    Args:
      name:  A name for this `Op`.

    Returns:
      Shape `[B1,...,Bb]` `Tensor` of same `dtype` as `self`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    exit(self._trace())
