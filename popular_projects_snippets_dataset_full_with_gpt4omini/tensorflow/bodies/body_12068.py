# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for Pad."""
# Pad introduces values around the original tensor, so the gradient function
# slices the original shape out of the gradient."""
x = op.inputs[0]
a = op.inputs[1]  # [Rank(x), 2]
# Takes a slice of a. The 1st column. [Rank(x), 1].
pad_before = array_ops.slice(a, [0, 0],
                             array_ops.stack([array_ops.rank(x), 1]))
# Make it a 1-D tensor.
begin = array_ops.reshape(pad_before, [-1])
sizes = array_ops.shape(x, out_type=begin.dtype)
x_grad = array_ops.slice(grad, begin, sizes)
if len(op.inputs) == 3:
    exit((x_grad, None, None))
else:
    exit((x_grad, None))
