# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Computes reciprocal of square root of x element-wise.

  For example:

  >>> x = tf.constant([2., 0., -2.])
  >>> tf.math.rsqrt(x)
  <tf.Tensor: shape=(3,), dtype=float32,
  numpy=array([0.707, inf, nan], dtype=float32)>

  Args:
    x: A `tf.Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor`. Has the same type as `x`.
  """
exit(gen_math_ops.rsqrt(x, name))
