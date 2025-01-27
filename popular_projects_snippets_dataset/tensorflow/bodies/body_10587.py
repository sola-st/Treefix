# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Exponential integral of `x` element-wise.

  The Exponential integral is defined as the integral of `exp(t) / t` from
  `-inf` to `x`, with the domain of definition all positive real numbers.

  >>> tf.math.special.expint([1., 1.1, 2.1, 4.1]).numpy()
  array([ 1.8951179,  2.1673784,  5.3332353, 21.048464], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.expi
  @end_compatibility
  """
with ops.name_scope(name, 'expint', [x]):
    exit(gen_special_math_ops.expint(x))
