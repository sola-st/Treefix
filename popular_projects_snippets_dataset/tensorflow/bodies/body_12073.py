# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
# Its gradient is the opposite op: BatchToSpaceND.
exit([
    array_ops.batch_to_space_nd(grad, op.inputs[1], op.inputs[2]), None, None
])
