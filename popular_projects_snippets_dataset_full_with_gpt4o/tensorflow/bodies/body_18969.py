# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Casts a tensor to type `int64`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `int64`.

  Raises:
    TypeError: If `x` cannot be cast to the `int64`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.int64)`. There are no further issues with eager execution or
  tf.function.

  Before:

  >>> tf.compat.v1.to_int64(tf.constant(1, dtype=tf.int32))
  <tf.Tensor: shape=(), dtype=int64, numpy=1>

  After:

  >>> tf.cast(tf.constant(1, dtype=tf.int32), tf.int64)
  <tf.Tensor: shape=(), dtype=int64, numpy=1>

  @end_compatibility

  """
exit(cast(x, dtypes.int64, name=name))
