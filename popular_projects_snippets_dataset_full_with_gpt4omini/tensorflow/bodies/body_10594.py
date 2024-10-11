# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel i1e function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_i1e([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.20791042, -0.15642083,  0.15642083,  0.20791042], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i1e
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_i1e', [x]):
    exit(gen_special_math_ops.bessel_i1e(x))
