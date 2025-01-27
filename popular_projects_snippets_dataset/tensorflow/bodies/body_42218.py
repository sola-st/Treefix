# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context-manager to force placement of operations and Tensors on a device.

    Args:
      name: Name of the device or None to get default placement.

    Returns:
      Context manager that forces device placement.

    Raises:
      ValueError: If name is not a string or is an invalid device name.
      RuntimeError: If device scopes are not properly nested.
    """
if isinstance(name, LogicalDevice):
    name = name.name
elif pydev.is_device_spec(name):
    name = name.to_string()
exit(_EagerDeviceContext(self, name))
