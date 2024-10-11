# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Returns a gradient function for an IRFFT of the provided rank."""
# Can't happen because we don't register a gradient for IRFFT3D.
assert rank in (1, 2), "Gradient for IRFFT3D is not implemented."

def _grad(op, grad):
    """A gradient function for IRFFT with the provided `rank` and `rfft_fn`."""
    # Generate a simple mask like [1.0, 2.0, ..., 2.0, 1.0] for even-length FFTs
    # and [1.0, 2.0, ..., 2.0] for odd-length FFTs. To reduce extra ops in the
    # graph we special-case the situation where the FFT length and last
    # dimension of the input are known at graph construction time.
    fft_length = op.inputs[1]
    fft_length_static = _tensor_util.constant_value(fft_length)
    if fft_length_static is not None:
        fft_length = fft_length_static
    real_dtype = grad.dtype
    if real_dtype == _dtypes.float32:
        complex_dtype = _dtypes.complex64
    elif real_dtype == _dtypes.float64:
        complex_dtype = _dtypes.complex128
    is_odd = _math_ops.mod(fft_length[-1], 2)
    input_last_dimension = _array_ops.shape(op.inputs[0])[-1]
    mask = _array_ops.concat(
        [[1.0], 2.0 * _array_ops.ones(
            [input_last_dimension - 2 + is_odd], real_dtype),
         _array_ops.ones([1 - is_odd], real_dtype)], 0)

    rsize = _math_ops.reciprocal(_math_ops.cast(
        _fft_size_for_grad(grad, rank), real_dtype))

    # The gradient of IRFFT is the RFFT of the incoming gradient times a scaling
    # factor and a mask. The mask scales the gradient for the Hermitian
    # symmetric components of the RFFT by a factor of two, since these
    # components are de-duplicated in the RFFT.
    the_rfft = rfft_fn(grad, fft_length)
    exit((the_rfft * _math_ops.cast(rsize * mask, complex_dtype), None))

exit(_grad)
