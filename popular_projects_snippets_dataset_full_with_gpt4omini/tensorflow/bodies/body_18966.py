# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Casts a tensor to type `float32`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `float32`.

  Raises:
    TypeError: If `x` cannot be cast to the `float32`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.float32)`. There are no further issues with eager execution
  or tf.function.

  Before:

  >>> tf.compat.v1.to_float(tf.constant(3.14, dtype=tf.double))
  <tf.Tensor: shape=(), dtype=float32, numpy=3.14>

  After:

  >>> tf.cast(tf.constant(3.14, dtype=tf.double), tf.float32)
  <tf.Tensor: shape=(), dtype=float32, numpy=3.14>

  @end_compatibility

  """
exit(cast(x, dtypes.float32, name=name))
