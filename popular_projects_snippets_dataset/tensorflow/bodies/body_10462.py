# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for SegmentMean."""
input_rank = array_ops.rank(op.inputs[0])
ones_shape = array_ops.concat([
    array_ops.shape(op.inputs[1]),
    array_ops.ones(
        array_ops.expand_dims(input_rank - 1, 0), dtype=dtypes.int32)
], 0)
ones = array_ops.ones(ones_shape, dtype=grad.dtype)
scaled_grad = math_ops.divide(grad, math_ops.segment_sum(ones, op.inputs[1]))
exit((array_ops.gather(scaled_grad, op.inputs[1]), None))
