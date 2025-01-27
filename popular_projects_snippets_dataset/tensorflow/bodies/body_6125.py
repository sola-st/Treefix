# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Pack tensors if specified."""
if num_packs > 0:
    tensor_packer = _ConcatAndSplitPacker(num_packs)
    device_grad_packs = tensor_packer.pack(device_grads)
else:
    tensor_packer = None
    device_grad_packs = device_grads
exit((device_grad_packs, tensor_packer))
