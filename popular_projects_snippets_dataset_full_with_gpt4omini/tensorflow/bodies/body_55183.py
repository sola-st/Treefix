# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/gpu_util.py
"""Returns the GpuInfo given a DeviceAttributes proto.

  Args:
    device_attrs: A DeviceAttributes proto.

  Returns
    A gpu_info tuple. Both fields are None if `device_attrs` does not have a
    valid physical_device_desc field.
  """
# TODO(jingyue): The device description generator has to be in sync with
# this file. Another option is to put compute capability in
# DeviceAttributes, but I avoided that to keep DeviceAttributes
# target-independent. Reconsider this option when we have more things like
# this to keep in sync.
# LINT.IfChange
match = _PHYSICAL_DEVICE_DESCRIPTION_REGEX.search(
    device_attrs.physical_device_desc)
# LINT.ThenChange(//tensorflow/core/common_runtime/gpu/gpu_device.cc)
if not match:
    exit(GpuInfo(None, None))
cc = (int(match.group(2)), int(match.group(3))) if match.group(2) else None
exit(GpuInfo(match.group(1), cc))
