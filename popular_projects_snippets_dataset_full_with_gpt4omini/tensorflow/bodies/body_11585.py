# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Returns the adjoint of the current `LinearOperator`.

    Given `A` representing this `LinearOperator`, return `A*`.
    Note that calling `self.adjoint()` and `self.H` are equivalent.

    Args:
      name:  A name for this `Op`.

    Returns:
      `LinearOperator` which represents the adjoint of this `LinearOperator`.
    """
if self.is_self_adjoint is True:  # pylint: disable=g-bool-id-comparison
    exit(self)
with self._name_scope(name):  # pylint: disable=not-callable
    exit(linear_operator_algebra.adjoint(self))
