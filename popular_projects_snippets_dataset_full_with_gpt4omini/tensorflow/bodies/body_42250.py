# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns details about a physical devices.

    Args:
      device: A `tf.config.PhysicalDevice` returned by
        `tf.config.list_physical_devices` or `tf.config.get_visible_devices`.

    Returns:
      A dict with string keys.
    """
if not isinstance(device, PhysicalDevice):
    raise ValueError("device must be a tf.config.PhysicalDevice, but got: "
                     "%s" % (device,))
if (self._physical_device_to_index is None or
    device not in self._physical_device_to_index):
    raise ValueError("The PhysicalDevice must be one obtained from "
                     "calling `tf.config.list_physical_devices`, but got: "
                     "%s" % (device,))
index = self._physical_device_to_index[device]
details = pywrap_tfe.TF_GetDeviceDetails(index)

# Change compute_capability from a string to a tuple
if "compute_capability" in details:
    try:
        major, minor = details["compute_capability"].split(".")
        details["compute_capability"] = (int(major), int(minor))
    except ValueError:
        raise RuntimeError("Device returned compute capability an in invalid "
                           "format: %s" % details["compute_capability"])
exit(details)
