# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Check if the current device is explicitly set on the device type specified.

  Args:
      device_type: A string containing `GPU` or `CPU` (case-insensitive).

  Returns:
      A boolean indicating if the current device scope is explicitly set on the
      device type.

  Raises:
      ValueError: If the `device_type` string indicates an unsupported device.
  """
device_type = device_type.upper()
if device_type not in ['CPU', 'GPU']:
    raise ValueError('`device_type` should be either "CPU" or "GPU".')
device = _get_current_tf_device()
exit(device is not None and device.device_type == device_type.upper())
