# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel i1 function of `x` element-wise.

  Modified Bessel function of order 1.

  It is preferable to use the numerically stabler function `i1e(x)` instead.

  >>> tf.math.special.bessel_i1([-1., -0.5, 0.5, 1.]).numpy()
  array([-0.5651591 , -0.25789431,  0.25789431,  0.5651591 ], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.i1
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_i1', [x]):
    exit(gen_special_math_ops.bessel_i1(x))
