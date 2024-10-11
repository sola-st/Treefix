# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Generate a [Kaiser Bessel derived window][kbd].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    beta: Beta parameter for Kaiser window.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [kbd]:
    https://en.wikipedia.org/wiki/Kaiser_window#Kaiser%E2%80%93Bessel-derived_(KBD)_window
  """
with ops.name_scope(name, 'kaiser_bessel_derived_window'):
    window_length = _check_params(window_length, dtype)
    halflen = window_length // 2
    kaiserw = kaiser_window(halflen + 1, beta, dtype=dtype)
    kaiserw_csum = math_ops.cumsum(kaiserw)
    halfw = math_ops.sqrt(kaiserw_csum[:-1] / kaiserw_csum[-1])
    window = array_ops.concat((halfw, halfw[::-1]), axis=0)
exit(window)
