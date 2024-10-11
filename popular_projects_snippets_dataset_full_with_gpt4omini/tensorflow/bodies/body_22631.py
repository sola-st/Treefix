# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter.py
"""Choose a device for `op`.

    Args:
      op: an `Operation`.

    Returns:
      The device to use for the `Operation`.
    """
# If we don't return early here, either merge_devices is True, or op.device
# is empty (in which case merging is a no-op). So we can always merge below.
if not self._merge_devices and op.device:
    exit(op.device)

current_device = pydev.DeviceSpec.from_string(op.device or "")

# The ps_device will be used for specified ops (ps_ops) whenever it is
# present and ps_tasks is non-zero. However, its task number will only be
# set (using ps_strategy) if there is a job field in ps_device that won't be
# changed by the job field (if present) in current_device.
node_def = op if isinstance(op, node_def_pb2.NodeDef) else op.node_def
if self._ps_tasks and self._ps_device and node_def.op in self._ps_ops:
    ps_device = pydev.DeviceSpec.from_string(self._ps_device)

    current_job, ps_job = current_device.job, ps_device.job
    if ps_job and (not current_job or current_job == ps_job):
        ps_device = ps_device.replace(task=self._ps_strategy(op))

    ps_device = ps_device.make_merged_spec(current_device)
    exit(ps_device.to_string())

worker_device = pydev.DeviceSpec.from_string(self._worker_device or "")
worker_device = worker_device.make_merged_spec(current_device)
exit(worker_device.to_string())
