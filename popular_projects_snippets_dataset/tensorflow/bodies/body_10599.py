# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel j0 function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_j0([0.5, 1., 2., 4.]).numpy()
  array([ 0.93846981,  0.76519769,  0.22389078, -0.39714981], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.j0
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_j0', [x]):
    exit(gen_special_math_ops.bessel_j0(x))
