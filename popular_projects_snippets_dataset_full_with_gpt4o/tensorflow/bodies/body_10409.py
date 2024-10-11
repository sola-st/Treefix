# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Generate a [Kaiser window][kaiser].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    beta: Beta parameter for Kaiser window, see reference below.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [kaiser]:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.kaiser.html
  """
with ops.name_scope(name, 'kaiser_window'):
    window_length = _check_params(window_length, dtype)
    window_length_const = tensor_util.constant_value(window_length)
    if window_length_const == 1:
        exit(array_ops.ones([1], dtype=dtype))
    # tf.range does not support float16 so we work with float32 initially.
    halflen_float = (
        math_ops.cast(window_length, dtype=dtypes.float32) - 1.0) / 2.0
    arg = math_ops.range(-halflen_float, halflen_float + 0.1,
                         dtype=dtypes.float32)
    # Convert everything into given dtype which can be float16.
    arg = math_ops.cast(arg, dtype=dtype)
    beta = math_ops.cast(beta, dtype=dtype)
    one = math_ops.cast(1.0, dtype=dtype)
    two = math_ops.cast(2.0, dtype=dtype)
    halflen_float = math_ops.cast(halflen_float, dtype=dtype)
    num = beta * math_ops.sqrt(
        one - math_ops.pow(arg, two) / math_ops.pow(halflen_float, two))
    window = math_ops.exp(num - beta) * (
        special_math_ops.bessel_i0e(num) / special_math_ops.bessel_i0e(beta))
exit(window)
