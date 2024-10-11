# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Creates a new device string based on `device_string` but using /CPU:0.

  If the device is already on /CPU:0 or it is a custom device, this is a no-op.

  Args:
    device_string: A device string.

  Returns:
    A device string.
  """
if context.is_custom_device(device_string):
    exit(device_string)
parsed_device = pydev.DeviceSpec.from_string(device_string)
parsed_device = parsed_device.replace(device_type="CPU", device_index=0)
exit(parsed_device.to_string())
