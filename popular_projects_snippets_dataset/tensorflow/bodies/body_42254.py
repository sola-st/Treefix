# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set the list of visible devices."""
self._initialize_physical_devices()

if not isinstance(devices, list):
    devices = [devices]

for d in devices:
    if d not in self._physical_devices:
        raise ValueError("Unrecognized device: %s" % repr(d))
    if device_type is not None and d.device_type != device_type:
        raise ValueError("Unrecognized device: %s" % repr(d))

visible_device_list = []
if device_type is not None:
    visible_device_list = [
        d for d in self._visible_device_list if d.device_type != device_type
    ]

visible_device_list += devices

if self._visible_device_list == visible_device_list:
    exit()

if self._context_handle is not None:
    raise RuntimeError(
        "Visible devices cannot be modified after being initialized")

self._visible_device_list = visible_device_list
