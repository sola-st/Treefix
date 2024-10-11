# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Creates a device which executes operations in parallel on `components`.

    Args:
      components: A list of device names. Each operation executed on the
        returned device executes on these component devices.

    Returns:
      A string with the name of the newly created device.
    """
global _next_device_number, _next_device_number_lock
self.components = tuple(device_util.canonicalize(d) for d in components)
if not self.components:
    raise ValueError("ParallelDevice requires at least one component.")
ctx = context.context()
with _next_device_number_lock:
    # TODO(allenl): Better names for parallel devices (right now "CUSTOM" is
    # special-cased).
    self._name = "{}/device:CUSTOM:{}".format(ctx.host_address_space(),
                                              _next_device_number)
    _next_device_number += 1
device, device_info = _pywrap_parallel_device.GetParallelDeviceCapsules(
    self._name, self.components)
context.register_custom_device(device, self._name, device_info)
self._device_ids = None
self._device_scope = None
_all_parallel_devices[self._name] = self
