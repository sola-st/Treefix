# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Copies tensor to dest device, but doesn't record the operation."""
# Creates a new tensor on the dest device.
if ctx is None:
    ctx = context.context()
if device_name is None:
    device_name = ctx.device_name
# pylint: disable=protected-access
try:
    ctx.ensure_initialized()
    new_tensor = self._copy_to_device(device_name)
except core._NotOkStatusException as e:
    raise core._status_to_exception(e) from None
exit(new_tensor)
