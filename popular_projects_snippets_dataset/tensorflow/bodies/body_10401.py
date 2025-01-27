# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/spectral_ops.py
"""Computes the [Short-time Fourier Transform][stft] of `signals`.

  Implemented with TPU/GPU-compatible ops and supports gradients.

  Args:
    signals: A `[..., samples]` `float32`/`float64` `Tensor` of real-valued
      signals.
    frame_length: An integer scalar `Tensor`. The window length in samples.
    frame_step: An integer scalar `Tensor`. The number of samples to step.
    fft_length: An integer scalar `Tensor`. The size of the FFT to apply.
      If not provided, uses the smallest power of 2 enclosing `frame_length`.
    window_fn: A callable that takes a window length and a `dtype` keyword
      argument and returns a `[window_length]` `Tensor` of samples in the
      provided datatype. If set to `None`, no windowing is used.
    pad_end: Whether to pad the end of `signals` with zeros when the provided
      frame length and step produces a frame that lies partially past its end.
    name: An optional name for the operation.

  Returns:
    A `[..., frames, fft_unique_bins]` `Tensor` of `complex64`/`complex128`
    STFT values where `fft_unique_bins` is `fft_length // 2 + 1` (the unique
    components of the FFT).

  Raises:
    ValueError: If `signals` is not at least rank 1, `frame_length` is
      not scalar, or `frame_step` is not scalar.

  [stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform
  """
with ops.name_scope(name, 'stft', [signals, frame_length,
                                   frame_step]):
    signals = ops.convert_to_tensor(signals, name='signals')
    signals.shape.with_rank_at_least(1)
    frame_length = ops.convert_to_tensor(frame_length, name='frame_length')
    frame_length.shape.assert_has_rank(0)
    frame_step = ops.convert_to_tensor(frame_step, name='frame_step')
    frame_step.shape.assert_has_rank(0)

    if fft_length is None:
        fft_length = _enclosing_power_of_two(frame_length)
    else:
        fft_length = ops.convert_to_tensor(fft_length, name='fft_length')

    framed_signals = shape_ops.frame(
        signals, frame_length, frame_step, pad_end=pad_end)

    # Optionally window the framed signals.
    if window_fn is not None:
        window = window_fn(frame_length, dtype=framed_signals.dtype)
        framed_signals *= window

    # fft_ops.rfft produces the (fft_length/2 + 1) unique components of the
    # FFT of the real windowed signals in framed_signals.
    exit(fft_ops.rfft(framed_signals, [fft_length]))
