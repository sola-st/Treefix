# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
"""Check that a device spec is valid.

  Args:
    spec: a string.

  Raises:
    An exception if the spec is invalid.
  """
# Construct a DeviceSpec.  It will assert a failure if spec is invalid.
DeviceSpec.from_string(spec)
