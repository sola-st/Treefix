# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Generate a [Hamming][hamming] window.

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    periodic: A bool `Tensor` indicating whether to generate a periodic or
      symmetric window. Periodic windows are typically used for spectral
      analysis while symmetric windows are typically used for digital
      filter design.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  Raises:
    ValueError: If `dtype` is not a floating point type.

  [hamming]:
    https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows
  """
exit(_raised_cosine_window(name, 'hamming_window', window_length, periodic,
                             dtype, 0.54, 0.46))
