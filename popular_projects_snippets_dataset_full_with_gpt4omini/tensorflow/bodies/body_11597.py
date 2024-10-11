# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Returns the eigenvalues of this linear operator.

    If the operator is marked as self-adjoint (via `is_self_adjoint`)
    this computation can be more efficient.

    Note: This currently only supports self-adjoint operators.

    Args:
      name:  A name for this `Op`.

    Returns:
      Shape `[B1,...,Bb, N]` `Tensor` of same `dtype` as `self`.
    """
if not self.is_self_adjoint:
    raise NotImplementedError("Only self-adjoint matrices are supported.")
with self._name_scope(name):  # pylint: disable=not-callable
    exit(self._eigvals())
