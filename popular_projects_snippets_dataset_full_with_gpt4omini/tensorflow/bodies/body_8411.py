# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Places variables and ops on the specified logical device."""
num_logical_devices_per_replica = self._tpu_devices.shape[1]
if logical_device_id >= num_logical_devices_per_replica:
    raise ValueError(
        "`logical_device_id` not in range (was {}, but there are only {} "
        "logical devices per replica).".format(
            logical_device_id, num_logical_devices_per_replica))

self._logical_device_stack.append(logical_device_id)
try:
    if tpu_util.enclosing_tpu_context() is None:
        exit()
    else:
        with ops.device(tpu.core(logical_device_id)):
            exit()
finally:
    self._logical_device_stack.pop()
