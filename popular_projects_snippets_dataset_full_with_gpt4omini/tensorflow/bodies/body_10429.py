# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/fft_ops.py
expanded = _array_ops.reshape(
    matrix,
    _array_ops.concat([
        _array_ops.ones([_array_ops.rank(t) - 2], _dtypes.int32),
        _array_ops.shape(matrix)
    ], 0))
exit(_array_ops.tile(
    expanded, _array_ops.concat([_array_ops.shape(t)[:-2], [1, 1]], 0)))
