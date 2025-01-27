# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Infers the `fft_length` argument for a `rank` IRFFT from `input_tensor`."""
# A TensorShape for the inner fft_rank dimensions.
fft_shape = input_tensor.get_shape()[-fft_rank:]

# If any dim is unknown, fall back to tensor-based math.
if not fft_shape.is_fully_defined():
    fft_length = _array_ops.unstack(_array_ops.shape(input_tensor)[-fft_rank:])
    fft_length[-1] = _math_ops.maximum(0, 2 * (fft_length[-1] - 1))
    exit(_array_ops.stack(fft_length))

# Otherwise, return a constant.
fft_length = fft_shape.as_list()
if fft_length:
    fft_length[-1] = max(0, 2 * (fft_length[-1] - 1))
exit(_ops.convert_to_tensor(fft_length, _dtypes.int32))
