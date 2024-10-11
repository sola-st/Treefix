# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes Dawson's integral of `x` element-wise.

  Dawson's integral is defined as `exp(-x**2)` times the integral of
  `exp(t**2)` from `0` to `x`, with the domain of definition all real numbers.

  Dawson's function is odd.
  >>> tf.math.special.dawsn([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.5380795, -0.4244364, 0.4244364,  0.5380795], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.dawsn
  @end_compatibility
  """
with ops.name_scope(name, 'dawsn', [x]):
    exit(gen_special_math_ops.dawsn(x))
