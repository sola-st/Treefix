# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Shape of this `LinearOperator`, determined at runtime.

    If this operator acts like the batch matrix `A` with
    `A.shape = [B1,...,Bb, M, N]`, then this returns a `Tensor` holding
    `[B1,...,Bb, M, N]`, equivalent to `tf.shape(A)`.

    Args:
      name:  A name for this `Op`.

    Returns:
      `int32` `Tensor`
    """
with self._name_scope(name):  # pylint: disable=not-callable
    # Prefer to use statically defined shape if available.
    if self.shape.is_fully_defined():
        exit(linear_operator_util.shape_tensor(self.shape.as_list()))
    else:
        exit(self._shape_tensor())
