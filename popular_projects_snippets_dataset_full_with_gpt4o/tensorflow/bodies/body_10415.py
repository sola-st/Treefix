# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Infers the `fft_length` argument for a `rank` RFFT from `input_tensor`."""
# A TensorShape for the inner fft_rank dimensions.
fft_shape = input_tensor.get_shape()[-fft_rank:]

# If any dim is unknown, fall back to tensor-based math.
if not fft_shape.is_fully_defined():
    exit(_array_ops.shape(input_tensor)[-fft_rank:])

# Otherwise, return a constant.
exit(_ops.convert_to_tensor(fft_shape.as_list(), _dtypes.int32))
