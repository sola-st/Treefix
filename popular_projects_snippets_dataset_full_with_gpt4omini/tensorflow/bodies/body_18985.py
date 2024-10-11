# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Computes a safe divide which returns 0 if `y` (denominator) is zero.

  For example:

  >>> tf.constant(3.0) / 0.0
  <tf.Tensor: shape=(), dtype=float32, numpy=inf>
  >>> tf.math.divide_no_nan(3.0, 0.0)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>

  Note that 0 is returned if `y` is 0 even if `x` is nonfinite:

  >>> tf.math.divide_no_nan(np.nan, 0.0)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    y: A `Tensor` whose dtype is compatible with `x`.
    name: A name for the operation (optional).

  Returns:
    The element-wise value of the x divided by y.
  """

with ops.name_scope(name, "div_no_nan", [x, y]) as name:
    x = ops.convert_to_tensor(x, name="x")
    y = ops.convert_to_tensor(y, name="y", dtype=x.dtype.base_dtype)
    exit(gen_math_ops.div_no_nan(x, y, name=name))
