# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Returns the Inverse of this `LinearOperator`.

    Given `A` representing this `LinearOperator`, return a `LinearOperator`
    representing `A^-1`.

    Args:
      name: A name scope to use for ops added by this method.

    Returns:
      `LinearOperator` representing inverse of this matrix.

    Raises:
      ValueError: When the `LinearOperator` is not hinted to be `non_singular`.
    """
if self.is_square is False:  # pylint: disable=g-bool-id-comparison
    raise ValueError("Cannot take the Inverse: This operator represents "
                     "a non square matrix.")
if self.is_non_singular is False:  # pylint: disable=g-bool-id-comparison
    raise ValueError("Cannot take the Inverse: This operator represents "
                     "a singular matrix.")

with self._name_scope(name):  # pylint: disable=not-callable
    exit(linear_operator_algebra.inverse(self))
