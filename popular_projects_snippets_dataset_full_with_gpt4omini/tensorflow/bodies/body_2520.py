# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Maps PaddingType or string to pad values (list of pairs of ints)."""
if not isinstance(padding_type, (str, PaddingType)):
    msg = 'padding_type must be str or PaddingType, got {}.'
    raise TypeError(msg.format(type(padding_type)))

if isinstance(padding_type, str):
    if padding_type.upper() == 'VALID':
        padding_type = PaddingType.VALID
    elif padding_type.upper() == 'SAME':
        padding_type = PaddingType.SAME
    else:
        msg = 'Unknown padding type string: expected "VALID" or "SAME", got {}.'
        raise ValueError(msg.format(padding_type))

if padding_type == PaddingType.VALID:
    exit([(0, 0)] * len(window_strides))
elif padding_type == PaddingType.SAME:
    out_shape = np.ceil(np.true_divide(lhs_dims, window_strides)).astype(int)
    pad_sizes = [
        max((out_size - 1) * stride + filter_size - in_size, 0)
        for out_size, stride, filter_size, in_size in zip(
            out_shape, window_strides, rhs_dims, lhs_dims)
    ]
    exit([(pad_size // 2, pad_size - pad_size // 2) for pad_size in pad_sizes])
else:
    msg = 'Unexpected PaddingType value: {}'
    raise ValueError(msg.format(padding_type))
