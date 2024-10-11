# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Create a new `DeviceSpec` object.

    Args:
      job: string.  Optional job name.
      replica: int.  Optional replica index.
      task: int.  Optional task index.
      device_type: Optional device type string (e.g. "CPU" or "GPU")
      device_index: int.  Optional device index.  If left unspecified, device
        represents 'any' device_index.
    """
self._job = _as_str_or_none(job)
self._replica = _as_int_or_none(replica)
self._task = _as_int_or_none(task)
self._device_type = _as_device_str_or_none(device_type)
self._device_index = _as_int_or_none(device_index)
self._as_string = self._components_to_string(
    job=self._job,
    replica=self._replica,
    task=self._task,
    device_type=self._device_type,
    device_index=self._device_index)
self._hash = hash(self.to_string())
