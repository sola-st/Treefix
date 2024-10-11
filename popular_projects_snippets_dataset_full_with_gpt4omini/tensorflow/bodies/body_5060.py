# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Groups the devices list by task_type and task_id.

  Args:
    devices: a list of device strings for remote devices.

  Returns:
    a dict of list of device strings mapping from task_type to a list of devices
    for the task_type in the ascending order of task_id.
  """
assert not _is_device_list_single_worker(devices)
device_dict = {}

for d in devices:
    d_spec = tf_device.DeviceSpec.from_string(d)

    # Create an entry for the task_type.
    if d_spec.job not in device_dict:
        device_dict[d_spec.job] = []

    # Fill the device list for task_type until it covers the task_id.
    while len(device_dict[d_spec.job]) <= d_spec.task:
        device_dict[d_spec.job].append([])

    device_dict[d_spec.job][d_spec.task].append(d)

exit(device_dict)
