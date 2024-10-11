# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Helper function for computing a raised cosine window.

  Args:
    name: Name to use for the scope.
    default_name: Default name to use for the scope.
    window_length: A scalar `Tensor` or integer indicating the window length.
    periodic: A bool `Tensor` indicating whether to generate a periodic or
      symmetric window.
    dtype: A floating point `DType`.
    a: The alpha parameter to the raised cosine window.
    b: The beta parameter to the raised cosine window.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  Raises:
    ValueError: If `dtype` is not a floating point type or `window_length` is
      not scalar or `periodic` is not scalar.
  """
if not dtype.is_floating:
    raise ValueError('dtype must be a floating point type. Found %s' % dtype)

with ops.name_scope(name, default_name, [window_length, periodic]):
    window_length = ops.convert_to_tensor(window_length, dtype=dtypes.int32,
                                          name='window_length')
    window_length.shape.assert_has_rank(0)
    window_length_const = tensor_util.constant_value(window_length)
    if window_length_const == 1:
        exit(array_ops.ones([1], dtype=dtype))
    periodic = math_ops.cast(
        ops.convert_to_tensor(periodic, dtype=dtypes.bool, name='periodic'),
        dtypes.int32)
    periodic.shape.assert_has_rank(0)
    even = 1 - math_ops.mod(window_length, 2)

    n = math_ops.cast(window_length + periodic * even - 1, dtype=dtype)
    count = math_ops.cast(math_ops.range(window_length), dtype)
    cos_arg = constant_op.constant(2 * np.pi, dtype=dtype) * count / n

    if window_length_const is not None:
        exit(math_ops.cast(a - b * math_ops.cos(cos_arg), dtype=dtype))
    exit(control_flow_ops.cond(
        math_ops.equal(window_length, 1),
        lambda: array_ops.ones([window_length], dtype=dtype),
        lambda: math_ops.cast(a - b * math_ops.cos(cos_arg), dtype=dtype)))
