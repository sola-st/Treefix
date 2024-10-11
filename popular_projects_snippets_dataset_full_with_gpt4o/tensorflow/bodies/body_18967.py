# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Casts a tensor to type `float64`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `float64`.

  Raises:
    TypeError: If `x` cannot be cast to the `float64`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.double)`. There are no further issues with eager execution or
  tf.function.

  Before:

  >>> tf.compat.v1.to_double(tf.constant(3.14, dtype=tf.float32))
  <tf.Tensor: shape=(), dtype=float64, numpy=3.14>

  After:

  >>> tf.cast(tf.constant(3.14, dtype=tf.float32), tf.double)
  <tf.Tensor: shape=(), dtype=float64, numpy=3.14>

  @end_compatibility

  """
exit(cast(x, dtypes.float64, name=name))
