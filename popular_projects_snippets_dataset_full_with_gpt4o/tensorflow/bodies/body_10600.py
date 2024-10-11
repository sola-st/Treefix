# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel j1 function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_j1([0.5, 1., 2., 4.]).numpy()
  array([ 0.24226846,  0.44005059,  0.57672481, -0.06604333], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.j1
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_j1', [x]):
    exit(gen_special_math_ops.bessel_j1(x))
