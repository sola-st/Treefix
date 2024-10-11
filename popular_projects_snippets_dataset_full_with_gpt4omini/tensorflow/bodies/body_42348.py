# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Calls TFE_IsCustomDevice.

  Enables using C extensions specifying a custom device from Python. See the
  experimental eager C API in tensorflow/c/eager/c_api_experimental.h for
  details.

  Args:
    device_name: A string indicating the name to check whether it is a
      registered custom device.

  Returns:
    A boolean.
  """
exit(context().is_custom_device(device_name))
