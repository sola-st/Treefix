# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Set the device of this operation.

    Args:
      device: string or device..  The device to set.
    """
self._set_device_from_string(compat.as_str(_device_string(device)))
