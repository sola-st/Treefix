# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for SparseSegmentMeanWithNumSegments."""
dim0 = array_ops.shape(op.inputs[0])[0]
exit((math_ops.sparse_segment_mean_grad(grad, op.inputs[1], op.inputs[2],
                                          dim0), None, None, None))
