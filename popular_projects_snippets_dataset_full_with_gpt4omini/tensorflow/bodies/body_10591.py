# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel i0 function of `x` element-wise.

  Modified Bessel function of order 0.

  It is preferable to use the numerically stabler function `i0e(x)` instead.

  >>> tf.math.special.bessel_i0([-1., -0.5, 0.5, 1.]).numpy()
  array([1.26606588, 1.06348337, 1.06348337, 1.26606588], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i0
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_i0', [x]):
    exit(gen_special_math_ops.bessel_i0(x))
