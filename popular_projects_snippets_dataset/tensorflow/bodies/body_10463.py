# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for SparseSegmentSum."""
dim0 = array_ops.shape(op.inputs[0])[0]
if compat.forward_compatible(2021, 6, 10):
    exit((math_ops.sparse_segment_sum_grad(grad, op.inputs[1], op.inputs[2],
                                             dim0), None, None))
else:
    exit((math_ops.unsorted_segment_sum(
        array_ops.gather(grad, op.inputs[2]), op.inputs[1], dim0), None, None))
