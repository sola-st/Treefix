# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes the Bessel y1 function of `x` element-wise.

  Modified Bessel function of order 1.

  >>> tf.math.special.bessel_y1([0.5, 1., 2., 4.]).numpy()
  array([-1.47147239, -0.78121282, -0.10703243,  0.39792571], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.y1
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_y1', [x]):
    exit(gen_special_math_ops.bessel_y1(x))
