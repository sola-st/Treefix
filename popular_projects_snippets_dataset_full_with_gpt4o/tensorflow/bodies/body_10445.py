# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/dct_ops.py
rank = len(input.shape)
padding = [[0, 0] for _ in range(rank)]
padding[rank - 1][1] = n - seq_len
padding = _ops.convert_to_tensor(padding, dtype=_dtypes.int32)
exit(_array_ops.pad(input, paddings=padding))
