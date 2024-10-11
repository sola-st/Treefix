# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
exit(array_ops.transpose(
    tensor,
    array_ops.concat([
        math_ops.range(dim_index),
        math_ops.range(dim_index + 1, rank), [dim_index]
    ], 0)))
