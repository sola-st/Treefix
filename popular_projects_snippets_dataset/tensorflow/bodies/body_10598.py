# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel k1e function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_k1e([0.5, 1., 2., 4.]).numpy()
  array([2.73100971, 1.63615349, 1.03347685, 0.68157595], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k1e
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_k1e', [x]):
    exit(gen_special_math_ops.bessel_k1e(x))
