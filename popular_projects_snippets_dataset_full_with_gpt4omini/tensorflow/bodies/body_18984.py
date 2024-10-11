# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Divides x / y elementwise (using Python 2 division operator semantics).

  @compatibility(TF2)
  This function is deprecated in TF2. Prefer using the Tensor division operator,
  `tf.divide`, or `tf.math.divide`, which obey the Python 3 division operator
  semantics.
  @end_compatibility


  This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
  and `y` are both integers then the result will be an integer. This is in
  contrast to Python 3, where division with `/` is always a float while division
  with `//` is always an integer.

  Args:
    x: `Tensor` numerator of real numeric type.
    y: `Tensor` denominator of real numeric type.
    name: A name for the operation (optional).

  Returns:
    `x / y` returns the quotient of x and y.
  """
exit(_div_python2(x, y, name))
