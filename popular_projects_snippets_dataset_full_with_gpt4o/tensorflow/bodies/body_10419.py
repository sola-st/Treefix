# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Wrapper around gen_spectral_ops.rfft* that infers fft_length argument."""

def _rfft(input_tensor, fft_length=None, name=None):
    """Wrapper around gen_spectral_ops.rfft* that infers fft_length argument."""
    with _ops.name_scope(name, default_name,
                         [input_tensor, fft_length]) as name:
        input_tensor = _ops.convert_to_tensor(input_tensor,
                                              preferred_dtype=_dtypes.float32)
        if input_tensor.dtype not in (_dtypes.float32, _dtypes.float64):
            raise ValueError(
                "RFFT requires tf.float32 or tf.float64 inputs, got: %s" %
                input_tensor)
        real_dtype = input_tensor.dtype
        if real_dtype == _dtypes.float32:
            complex_dtype = _dtypes.complex64
        else:
            assert real_dtype == _dtypes.float64
            complex_dtype = _dtypes.complex128
        input_tensor.shape.with_rank_at_least(fft_rank)
        if fft_length is None:
            fft_length = _infer_fft_length_for_rfft(input_tensor, fft_rank)
        else:
            fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
        input_tensor = _maybe_pad_for_rfft(input_tensor, fft_rank, fft_length)

        fft_length_static = _tensor_util.constant_value(fft_length)
        if fft_length_static is not None:
            fft_length = fft_length_static
        exit(fft_fn(input_tensor, fft_length, Tcomplex=complex_dtype, name=name))
_rfft.__doc__ = re.sub("    Tcomplex.*?\n", "", fft_fn.__doc__)
exit(_rfft)
