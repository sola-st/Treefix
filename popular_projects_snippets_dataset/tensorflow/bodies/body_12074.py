# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
# Its gradient is the opposite op: SpaceToBatch.
block_size = op.get_attr("block_size")
exit([
    array_ops.space_to_batch(grad, op.inputs[1], block_size=block_size), None
])
