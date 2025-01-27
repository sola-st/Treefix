# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes Spence's integral of `x` element-wise.

  Spence's integral is defined as the integral of `log(t) / (1 - t)` from
  `1` to `x`, with the domain of definition all non-negative real numbers.

  >>> tf.math.special.spence([0.5, 1., 2., 3.]).numpy()
  array([ 0.58224034,  0.        , -0.82246685, -1.4367464], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.spence
  @end_compatibility
  """
with ops.name_scope(name, 'spence', [x]):
    exit(gen_special_math_ops.spence(x))
