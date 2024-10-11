# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel i0e function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_i0e([-1., -0.5, 0.5, 1.]).numpy()
  array([0.46575961, 0.64503527, 0.64503527, 0.46575961], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i0e
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_i0e', [x]):
    exit(gen_special_math_ops.bessel_i0e(x))
