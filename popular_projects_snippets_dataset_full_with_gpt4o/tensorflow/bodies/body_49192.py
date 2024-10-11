# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Segment-wise linear approximation of sigmoid.

  Faster than sigmoid.
  Returns `0.` if `x < -2.5`, `1.` if `x > 2.5`.
  In `-2.5 <= x <= 2.5`, returns `0.2 * x + 0.5`.

  Args:
      x: A tensor or variable.

  Returns:
      A tensor.
  """
point_two = _constant_to_tensor(0.2, x.dtype.base_dtype)
point_five = _constant_to_tensor(0.5, x.dtype.base_dtype)
x = math_ops.multiply(x, point_two)
x = math_ops.add(x, point_five)
x = clip_ops.clip_by_value(x, 0., 1.)
exit(x)
