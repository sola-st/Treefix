# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel k0 function of `x` element-wise.

  Modified Bessel function of order 0.

  It is preferable to use the numerically stabler function `k0e(x)` instead.

  >>> tf.math.special.bessel_k0([0.5, 1., 2., 4.]).numpy()
  array([0.92441907, 0.42102444, 0.11389387, 0.01115968], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k0
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_k0', [x]):
    exit(gen_special_math_ops.bessel_k0(x))
