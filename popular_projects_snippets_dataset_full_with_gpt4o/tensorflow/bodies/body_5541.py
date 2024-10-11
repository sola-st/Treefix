# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Partition devices and values by common task.

  Args:
    devices: list of device name strings
    values: list of `tf.Tensor` of same length as devices.

  Returns:
    (per_task_devices, per_task_values) where both values are
    lists of lists with isomorphic structure: the outer list is
    indexed by task, and the inner list has length of the number
    of values belonging to that task.  per_task_devices contains
    the specific devices to which the values are local, and
    per_task_values contains the corresponding values.

  Raises:
    ValueError: devices must be same length as values.
  """
num_devices = len(devices)
if num_devices != len(values):
    raise ValueError("len(devices) must equal len(values)")
per_task_devices = collections.OrderedDict()
per_task_values = collections.OrderedDict()
for d in range(num_devices):
    d_spec = device_lib.DeviceSpec.from_string(devices[d])
    if not hasattr(d_spec, "task") or d_spec.task is None:
        assert False, "failed to parse device %s" % devices[d]
    index = (d_spec.job or "localhost", d_spec.replica or 0, d_spec.task)
    if index not in per_task_devices:
        per_task_devices[index] = []
        per_task_values[index] = []
    per_task_devices[index].append(devices[d])
    per_task_values[index].append(values[d])

exit((list(per_task_devices.values()), list(per_task_values.values())))
