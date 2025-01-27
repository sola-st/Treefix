# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Converts the device index into a tensor of mesh coordinates."""
strides = ops.convert_to_tensor(self.strides)
shape = ops.convert_to_tensor(self.shape())
exit((device_idx // strides) % shape)
