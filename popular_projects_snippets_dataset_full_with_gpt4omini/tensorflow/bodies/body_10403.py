# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/spectral_ops.py
"""Generates a window function that can be used in `inverse_stft`.

  Constructs a window that is equal to the forward window with a further
  pointwise amplitude correction.  `inverse_stft_window_fn` is equivalent to
  `forward_window_fn` in the case where it would produce an exact inverse.

  See examples in `inverse_stft` documentation for usage.

  Args:
    frame_step: An integer scalar `Tensor`. The number of samples to step.
    forward_window_fn: window_fn used in the forward transform, `stft`.
    name: An optional name for the operation.

  Returns:
    A callable that takes a window length and a `dtype` keyword argument and
      returns a `[window_length]` `Tensor` of samples in the provided datatype.
      The returned window is suitable for reconstructing original waveform in
      inverse_stft.
  """
def inverse_stft_window_fn_inner(frame_length, dtype):
    """Computes a window that can be used in `inverse_stft`.

    Args:
      frame_length: An integer scalar `Tensor`. The window length in samples.
      dtype: Data type of waveform passed to `stft`.

    Returns:
      A window suitable for reconstructing original waveform in `inverse_stft`.

    Raises:
      ValueError: If `frame_length` is not scalar, `forward_window_fn` is not a
      callable that takes a window length and a `dtype` keyword argument and
      returns a `[window_length]` `Tensor` of samples in the provided datatype
      `frame_step` is not scalar, or `frame_step` is not scalar.
    """
    with ops.name_scope(name, 'inverse_stft_window_fn', [forward_window_fn]):
        frame_step_ = ops.convert_to_tensor(frame_step, name='frame_step')
        frame_step_.shape.assert_has_rank(0)
        frame_length = ops.convert_to_tensor(frame_length, name='frame_length')
        frame_length.shape.assert_has_rank(0)

        # Use equation 7 from Griffin + Lim.
        forward_window = forward_window_fn(frame_length, dtype=dtype)
        denom = math_ops.square(forward_window)
        overlaps = -(-frame_length // frame_step_)  # Ceiling division.  # pylint: disable=invalid-unary-operand-type
        denom = array_ops.pad(denom, [(0, overlaps * frame_step_ - frame_length)])
        denom = array_ops.reshape(denom, [overlaps, frame_step_])
        denom = math_ops.reduce_sum(denom, 0, keepdims=True)
        denom = array_ops.tile(denom, [overlaps, 1])
        denom = array_ops.reshape(denom, [overlaps * frame_step_])

        exit(forward_window / denom[:frame_length])
exit(inverse_stft_window_fn_inner)
