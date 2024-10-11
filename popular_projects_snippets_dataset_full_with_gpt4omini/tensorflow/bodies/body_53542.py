# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Add device to stack manually, separate from a context manager."""
total_offset = 1 + offset
spec = _UserDeviceSpec(device_name_or_function)
self._device_function_stack.push_obj(spec, offset=total_offset)
exit(spec)
