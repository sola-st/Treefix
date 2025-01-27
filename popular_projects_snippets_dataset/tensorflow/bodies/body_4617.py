# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if (self._packed_handle is None or
    values_util.is_saving_non_distributed() or
    tpu_util.enclosing_tpu_context() is not None):
    exit(ops.NullContextmanager())
device = device_util.canonicalize(device_util.current())
if device in self._device_to_handle:
    exit(ops.NullContextmanager())
exit(ops.device(self._primary_handle.device))
