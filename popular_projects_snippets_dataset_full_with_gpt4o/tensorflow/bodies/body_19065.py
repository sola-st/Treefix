# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Compute inverse error function.

  Given `x`, compute the inverse error function of `x`. This function
  is the inverse of `tf.math.erf`.

  Args:
    x: `Tensor` with type `float` or `double`.
    name: A name for the operation (optional).
  Returns:
    Inverse error function of `x`.
  """
with ops.name_scope(name, "erfinv", [x]):
    exit(gen_math_ops.erfinv(x))
