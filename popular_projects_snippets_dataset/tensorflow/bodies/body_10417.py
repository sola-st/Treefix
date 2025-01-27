# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
"""Pads `input_tensor` to `fft_length` on its inner-most `fft_rank` dims."""
fft_shape = _tensor_util.constant_value_as_shape(fft_length)

# Edge case: skip padding empty tensors.
if (input_tensor.shape.ndims is not None and
    any(dim.value == 0 for dim in input_tensor.shape.dims)):
    exit(input_tensor)

# If we know the shapes ahead of time, we can either skip or pre-compute the
# appropriate paddings. Otherwise, fall back to computing paddings in
# TensorFlow.
if fft_shape.is_fully_defined() and input_tensor.shape.ndims is not None:
    # Slice the last FFT-rank dimensions from input_tensor's shape.
    input_fft_shape = input_tensor.shape[-fft_shape.ndims:]  # pylint: disable=invalid-unary-operand-type

    if input_fft_shape.is_fully_defined():
        # In reverse, we only pad the inner-most dimension to fft_length / 2 + 1.
        if is_reverse:
            fft_shape = fft_shape[:-1].concatenate(
                fft_shape.dims[-1].value // 2 + 1)

        paddings = [[0, max(fft_dim.value - input_dim.value, 0)]
                    for fft_dim, input_dim in zip(
                        fft_shape.dims, input_fft_shape.dims)]
        if any(pad > 0 for _, pad in paddings):
            outer_paddings = [[0, 0]] * max((input_tensor.shape.ndims -
                                             fft_shape.ndims), 0)
            exit(_array_ops.pad(input_tensor, outer_paddings + paddings))
        exit(input_tensor)

  # If we can't determine the paddings ahead of time, then we have to pad. If
  # the paddings end up as zero, tf.pad has a special-case that does no work.
input_rank = _array_ops.rank(input_tensor)
input_fft_shape = _array_ops.shape(input_tensor)[-fft_rank:]
outer_dims = _math_ops.maximum(0, input_rank - fft_rank)
outer_paddings = _array_ops.zeros([outer_dims], fft_length.dtype)
# In reverse, we only pad the inner-most dimension to fft_length / 2 + 1.
if is_reverse:
    fft_length = _array_ops.concat([fft_length[:-1],
                                    fft_length[-1:] // 2 + 1], 0)
fft_paddings = _math_ops.maximum(0, fft_length - input_fft_shape)
paddings = _array_ops.concat([outer_paddings, fft_paddings], 0)
paddings = _array_ops.stack([_array_ops.zeros_like(paddings), paddings],
                            axis=1)
exit(_array_ops.pad(input_tensor, paddings))
