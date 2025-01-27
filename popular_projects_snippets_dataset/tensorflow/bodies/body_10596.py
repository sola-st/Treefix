# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel k0e function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_k0e([0.5, 1., 2., 4.]).numpy()
  array([1.52410939, 1.14446308, 0.84156822, 0.60929767], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k0e
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_k0e', [x]):
    exit(gen_special_math_ops.bessel_k0e(x))
