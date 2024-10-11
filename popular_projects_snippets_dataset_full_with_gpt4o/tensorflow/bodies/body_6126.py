# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Unpack tensors if they are packed before all-reduce."""
if tensor_packer:
    exit(tensor_packer.unpack(reduced))
exit(reduced)
