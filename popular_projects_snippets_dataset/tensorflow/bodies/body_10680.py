# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Encode inter-device transfers if the current device
    is not the same as the Staging Area's device.
    """

if not isinstance(tensors, (tuple, list)):
    tensors = [tensors]

curr_device_scope = control_flow_ops.no_op().device

if curr_device_scope != self._coloc_op.device:
    tensors = [array_ops.identity(t) for t in tensors]

exit(tensors)
