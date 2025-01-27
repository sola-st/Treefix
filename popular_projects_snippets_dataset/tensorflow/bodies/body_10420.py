# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Wrapper irfft* that infers fft_length argument."""
with _ops.name_scope(name, default_name,
                     [input_tensor, fft_length]) as name:
    input_tensor = _ops.convert_to_tensor(input_tensor,
                                          preferred_dtype=_dtypes.complex64)
    input_tensor.shape.with_rank_at_least(fft_rank)
    if input_tensor.dtype not in (_dtypes.complex64, _dtypes.complex128):
        raise ValueError(
            "IRFFT requires tf.complex64 or tf.complex128 inputs, got: %s" %
            input_tensor)
    complex_dtype = input_tensor.dtype
    real_dtype = complex_dtype.real_dtype
    if fft_length is None:
        fft_length = _infer_fft_length_for_irfft(input_tensor, fft_rank)
    else:
        fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    input_tensor = _maybe_pad_for_rfft(input_tensor, fft_rank, fft_length,
                                       is_reverse=True)
    fft_length_static = _tensor_util.constant_value(fft_length)
    if fft_length_static is not None:
        fft_length = fft_length_static
    exit(ifft_fn(input_tensor, fft_length, Treal=real_dtype, name=name))
