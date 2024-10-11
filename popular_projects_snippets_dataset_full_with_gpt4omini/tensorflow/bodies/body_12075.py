# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
# Its gradient is the opposite op: SpaceToBatchND.
exit([
    array_ops.space_to_batch_nd(grad, op.inputs[1], op.inputs[2]), None, None
])
