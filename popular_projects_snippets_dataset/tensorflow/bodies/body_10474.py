# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
""" Gradient for UnsortedSegmentMin and UnsortedSegmentMax. """
# Get the number of selected (minimum or maximum) elements in each segment.
gathered_outputs, zero_clipped_indices, is_positive = \
      _GatherDropNegatives(op.outputs[0], op.inputs[1])
is_selected = math_ops.equal(op.inputs[0], gathered_outputs)
is_selected = math_ops.logical_and(is_selected, is_positive)
num_selected = math_ops.unsorted_segment_sum(
    math_ops.cast(is_selected, grad.dtype), op.inputs[1], op.inputs[2])
# Compute the gradient for each segment. The gradient for the ith segment is
# divided evenly among the selected elements in that segment.
weighted_grads = math_ops.divide(grad, num_selected)
gathered_grads, _, _ = _GatherDropNegatives(weighted_grads, None,
                                            zero_clipped_indices, is_positive)
zeros = array_ops.zeros_like(gathered_grads)
exit((array_ops.where_v2(is_selected, gathered_grads, zeros), None, None))
