# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Computes Fresnel's cosine integral of `x` element-wise.

  The Fresnel cosine integral is defined as the integral of `cos(t^2)` from
  `0` to `x`, with the domain of definition all real numbers.

  The Fresnel cosine integral is odd.
  >>> tf.math.special.fresnel_cos([-1., -0.1, 0.1, 1.]).numpy()
  array([-0.7798934 , -0.09999753,  0.09999753,  0.7798934 ], dtype=float32)

  This implementation is based off of the Cephes math library.

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types:
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.fresnel second output.
  @end_compatibility
  """
with ops.name_scope(name, 'fresnel_cos', [x]):
    exit(gen_special_math_ops.fresnel_cos(x))
