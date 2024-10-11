# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Generate a [Vorbis power complementary window][vorbis].

  Args:
    window_length: A scalar `Tensor` indicating the window length to generate.
    dtype: The data type to produce. Must be a floating point type.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of shape `[window_length]` of type `dtype`.

  [vorbis]:
    https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform#Window_functions
  """
with ops.name_scope(name, 'vorbis_window'):
    window_length = _check_params(window_length, dtype)
    arg = math_ops.cast(math_ops.range(window_length), dtype=dtype)
    window = math_ops.sin(np.pi / 2.0 * math_ops.pow(math_ops.sin(
        np.pi / math_ops.cast(window_length, dtype=dtype) *
        (arg + 0.5)), 2.0))
exit(window)
