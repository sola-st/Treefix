# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns the resource on the local worker."""
current_device = device_util.canonicalize(device_util.current())
host_device = device_util.canonicalize(
    device_util.get_host_for_device(current_device))
exit(self._host_to_resources.get(
    host_device,
    self._host_to_resources[next(iter(self._host_to_resources))]))
