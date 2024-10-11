# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Swaps logits's dim_index and last_index."""
exit(array_ops.transpose(
    input_tensor,
    array_ops.concat([
        math_ops.range(dim_index), [last_index],
        math_ops.range(dim_index + 1, last_index), [dim_index]
    ], 0),
    name=name))
