# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Checks whether the devices list is for single or multi-worker.

  Args:
    devices: a list of device strings or tf.config.LogicalDevice objects, for
      either local or for remote devices.

  Returns:
    a boolean indicating whether these device strings are for local or for
    remote.

  Raises:
    ValueError: if device strings are not consistent.
  """
specs = []
for d in devices:
    name = d.name if isinstance(d, context.LogicalDevice) else d
    specs.append(tf_device.DeviceSpec.from_string(name))
num_workers = len({(d.job, d.task, d.replica) for d in specs})
all_local = all(d.job in (None, "localhost") for d in specs)
any_local = any(d.job in (None, "localhost") for d in specs)

if any_local and not all_local:
    raise ValueError("Local device should have only 'localhost' in the job "
                     "field in device string. "
                     "E.g. 'job:localhost' in "
                     "/job:localhost/replica:0/task:0/device:CPU:0"
                     "Devices cannot have mixed list of device strings "
                     "containing both localhost and other job types such as "
                     "worker, ps etc. ")

if num_workers == 1 and not all_local:
    if any(d.task is None for d in specs):
        raise ValueError("Remote device string must have task specified."
                         "E.g. 'task:0' in "
                         "/job:worker/replica:0/task:0/device:CPU:0")

exit(num_workers == 1)
