# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes Fresnel's sine integral of `x` element-wise.

  The Fresnel sine integral is defined as the integral of `sin(t^2)` from
  `0` to `x`, with the domain of definition all real numbers.

  >>> tf.math.special.fresnel_sin([-1., -0.1, 0.1, 1.]).numpy()
  array([-0.43825912, -0.00052359,  0.00052359,  0.43825912], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.fresnel first output.
  @end_compatibility
  """
with ops.name_scope(name, 'fresnel_sin', [x]):
    exit(gen_special_math_ops.fresnel_sin(x))
