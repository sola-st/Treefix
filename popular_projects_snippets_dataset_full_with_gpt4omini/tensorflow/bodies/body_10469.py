# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
""" Gradient for SegmentMin and SegmentMax. """
zeros = array_ops.zeros_like(op.inputs[0], dtype=op.inputs[0].dtype)
# Get the number of selected (minimum or maximum) elements in each segment.
gathered_outputs = array_ops.gather(op.outputs[0], op.inputs[1])
is_selected = math_ops.equal(op.inputs[0], gathered_outputs)
num_selected = math_ops.segment_sum(
    math_ops.cast(is_selected, grad.dtype), op.inputs[1])
# Compute the gradient for each segment. The gradient for the ith segment is
# divided evenly among the selected elements in that segment.
weighted_grads = math_ops.divide(grad, num_selected)
gathered_grads = array_ops.gather(weighted_grads, op.inputs[1])
exit((array_ops.where_v2(is_selected, gathered_grads, zeros), None))
