# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
"""Reads the value of this variable."""
if self.trainable:
    tape.variable_accessed(self)

handle = self.handle
if getattr(handle, "is_packed", False):
    # Add a device scope for a packed variable handle.
    with ops.device(self._get_on_device_or_primary().device):
        exit(gen_resource_variable_ops.read_variable_op(handle, self.dtype))
else:
    exit(gen_resource_variable_ops.read_variable_op(handle, self.dtype))
