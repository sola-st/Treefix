# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/system_info_lib.py
"""Gather list of devices available to TensorFlow.

  Returns:
    A list of test_log_pb2.AvailableDeviceInfo messages.
  """
device_info_list = []
devices = device_lib.list_local_devices()

for d in devices:
    device_info = test_log_pb2.AvailableDeviceInfo()
    device_info.name = d.name
    device_info.type = d.device_type
    device_info.memory_limit = d.memory_limit
    device_info.physical_description = d.physical_device_desc
    device_info_list.append(device_info)

exit(device_info_list)
