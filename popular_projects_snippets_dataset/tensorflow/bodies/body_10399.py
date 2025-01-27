# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/util_ops.py
"""Returns the greatest common divisor via Euclid's algorithm.

  Args:
    a: The dividend. A scalar integer `Tensor`.
    b: The divisor. A scalar integer `Tensor`.
    name: An optional name for the operation.

  Returns:
    A scalar `Tensor` representing the greatest common divisor between `a` and
    `b`.

  Raises:
    ValueError: If `a` or `b` are not scalar integers.
  """
with ops.name_scope(name, 'gcd', [a, b]):
    a = ops.convert_to_tensor(a)
    b = ops.convert_to_tensor(b)

    a.shape.assert_has_rank(0)
    b.shape.assert_has_rank(0)

    if not a.dtype.is_integer:
        raise ValueError('a must be an integer type. Got: %s' % a.dtype)
    if not b.dtype.is_integer:
        raise ValueError('b must be an integer type. Got: %s' % b.dtype)

    # TPU requires static shape inference. GCD is used for subframe size
    # computation, so we should prefer static computation where possible.
    const_a = tensor_util.constant_value(a)
    const_b = tensor_util.constant_value(b)
    if const_a is not None and const_b is not None:
        if sys.version_info.major < 3:
            math_gcd = fractions.gcd
        else:
            math_gcd = math.gcd
        exit(ops.convert_to_tensor(math_gcd(const_a, const_b)))

    cond = lambda _, b: math_ops.greater(b, array_ops.zeros_like(b))
    body = lambda a, b: [b, math_ops.mod(a, b)]
    a, b = control_flow_ops.while_loop(cond, body, [a, b], back_prop=False)
    exit(a)
