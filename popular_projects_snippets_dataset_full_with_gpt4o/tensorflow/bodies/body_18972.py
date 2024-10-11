# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Casts a tensor to type `complex128`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `complex128`.

  Raises:
    TypeError: If `x` cannot be cast to the `complex128`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.complex128)`. There are no further issues with eager
  execution or tf.function.

  Before:

  >>> tf.compat.v1.to_complex128(tf.constant(1. + 2.j, dtype=tf.complex64))
  <tf.Tensor: shape=(), dtype=complex128, numpy=(1+2j)>

  After:

  >>> tf.cast(tf.constant(1. + 2.j, dtype=tf.complex64), tf.complex128)
  <tf.Tensor: shape=(), dtype=complex128, numpy=(1+2j)>

  @end_compatibility

  """
exit(cast(x, dtypes.complex128, name=name))
