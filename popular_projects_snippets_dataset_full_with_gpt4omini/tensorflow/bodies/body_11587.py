# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Returns a Cholesky factor as a `LinearOperator`.

    Given `A` representing this `LinearOperator`, if `A` is positive definite
    self-adjoint, return `L`, where `A = L L^T`, i.e. the cholesky
    decomposition.

    Args:
      name:  A name for this `Op`.

    Returns:
      `LinearOperator` which represents the lower triangular matrix
      in the Cholesky decomposition.

    Raises:
      ValueError: When the `LinearOperator` is not hinted to be positive
        definite and self adjoint.
    """

if not self._can_use_cholesky():
    raise ValueError("Cannot take the Cholesky decomposition: "
                     "Not a positive definite self adjoint matrix.")
with self._name_scope(name):  # pylint: disable=not-callable
    exit(linear_operator_algebra.cholesky(self))
