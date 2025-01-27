# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Dimension (in the sense of vector spaces) of the range of this operator.

    Determined at runtime.

    If this operator acts like the batch matrix `A` with
    `A.shape = [B1,...,Bb, M, N]`, then this returns `M`.

    Args:
      name:  A name for this `Op`.

    Returns:
      `int32` `Tensor`
    """
# Derived classes get this "for free" once .shape() is implemented.
with self._name_scope(name):  # pylint: disable=not-callable
    exit(self._range_dimension_tensor())
