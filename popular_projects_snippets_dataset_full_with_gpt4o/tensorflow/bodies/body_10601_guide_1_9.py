name = 'bessel_y0_test' # pragma: no cover
gen_special_math_ops = type('MockGenSpecialMathOps', (object,), {'bessel_y0': lambda x: tf.raw_ops.BesselY0(x=x)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
from l3.Runtime import _l_
"""Computes the Bessel y0 function of `x` element-wise.

  Modified Bessel function of order 0.

  >>> tf.math.special.bessel_y0([0.5, 1., 2., 4.]).numpy()
  array([-0.44451873,  0.08825696,  0.51037567, -0.01694074], dtype=float32)

  Args:
    x: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.

  @compatibility(scipy)
  Equivalent to scipy.special.y0
  @end_compatibility
  """
with ops.name_scope(name, 'bessel_y0', [x]):
    _l_(22067)

    aux = gen_special_math_ops.bessel_y0(x)
    _l_(22066)
    exit(aux)
