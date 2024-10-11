# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel k1 function of `x` element-wise.

  Modified Bessel function of order 1.

  It is preferable to use the numerically stabler function `k1e(x)` instead.

  >>> tf.math.special.bessel_k1([0.5, 1., 2., 4.]).numpy()
  array([1.65644112, 0.60190723, 0.13986588, 0.0124835 ], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.k1
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_k1', [x]):
    exit(gen_special_math_ops.bessel_k1(x))
